from django.urls import path,include
from . import views
urlpatterns = [
    path('pay',views.paya,name = 'pay'),
    path('',views.home,name='home'),
    path('success',views.success,name='success'),
]
