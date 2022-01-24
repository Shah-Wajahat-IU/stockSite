
from django.urls import path
from .views import delete_stock, home,about,stock_data

urlpatterns = [
    path('',home,name="home"),
    path('about/',about,name="about"),
    path('stock/',stock_data,name="stock_data"),
    path('delete/<stock_id>', delete_stock,name='stock_delete')
]
