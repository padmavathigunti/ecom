
from django.urls import path
from . import views

urlpatterns = [
    path('product_field/',views.product_field,name ='Product_field'),
    path('data/',views.data,name = 'data'),
    path('User_field/',views.user_field,name = 'User_field'),
    path('buyed_product/',views.buyed_product,name = 'Buyed_product'),
    path('single_data/<pk>',views.single_data,name = 'single_data'),
    path('destroy/<pk>',views.destroy,name='destroy'),
    path('data1/',views.data1,name = 'data1'),
    path('destroy1/<pk>',views.destroy1,name='destroy1'),
    path('data2/<pk>',views.data2,name = 'data2'),

]
