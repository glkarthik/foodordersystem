from django.urls import path

from . import views

app_name = 'orders'
urlpatterns = [
    path('<str:order_id>/', views.OrderView, name='order'),
    path('', views.OrderSubmit, name='order_submit'),
]
