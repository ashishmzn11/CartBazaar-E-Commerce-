from django.contrib import admin
from django.urls import path
from . import views
urlpatterns = [
    # path('admin/', admin.site.urls),
    path('',views.index,name='shop'),
    path("about/", views.about, name="about"),  # About Page
    path("tracker/", views.tracker, name="tracker"),
    path("contact/", views.contact, name="contact"),
    path('search/',views.search,name='Search'),
    path('prodview/<int:id>/',views.productview,name='ProductView'),
    path('checkout/', views.checkout, name="checkout"),
    # path('placeorder/',views.placeorder,name='placeorder')
]