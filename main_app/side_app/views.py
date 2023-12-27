from django.views import View
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404
from side_app.models import Item
from dotenv import load_dotenv
import stripe
import os

load_dotenv()
stripe.api_key = os.getenv('STRIPE_SECRET_KEY')


class ItemView(View):
    def get(self, request, id):
        PUBLIC_STRIPE_KEY = os.getenv('PUBLIC_KEY')
        item = get_object_or_404(Item, id=id)
        return render(request, 'item.html', {'item': item, 'PUBLIC_KEY': PUBLIC_STRIPE_KEY})


class BuyView(View):
  def get(self, request, id):
      item = get_object_or_404(Item, id=id)
      session = stripe.checkout.Session.create(
          payment_method_types=['card'],
          line_items=[{
              'price_data': {
                  'currency': 'usd',
                  'product_data': {
                      'name': item.name,
                      'description': item.description,
                  },
                  'unit_amount': int(item.price * 100),
              },
              'quantity': 1,
          }],
          mode='payment',
          success_url='http://127.0.0.1:8000/thankyou',
          cancel_url='http://127.0.0.1:8000/cancel',
      )
      return JsonResponse({'session_id': session.id})

class SuccesBuy(View):
    def get(self, request):
        return render(request, 'thankyou.html')

class CancelBuy(View):
    def get(self, request):
        return render(request, 'cancel.html')