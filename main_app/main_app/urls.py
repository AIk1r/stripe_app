"""
URL configuration for main_app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from side_app.views import ItemView, BuyView, SuccesBuy, CancelBuy



urlpatterns = [
    path('admin/', admin.site.urls),
    path('item/<int:id>/', ItemView.as_view(), name='item_detail'),
    path('buy/<int:id>/', BuyView.as_view(), name='buy'),
    path('thankyou/', SuccesBuy.as_view(), name='thankyou'),
    path('cancel/', CancelBuy.as_view(), name='cancel'),
]
