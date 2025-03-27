from django.contrib import admin
from django.urls import path
from. import views

urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='shop'),
    path('about',views.about,name='AboutUs'),
    path('contact',views.contact,name='ContactUs'),
    path('tracker',views.tracker,name='TrackingStatus'),
    path('search',views.search,name='Search'),
    path('productView',views.productview,name='ProductView'),
    path('checkout',views.checkout,name='checkout')
]