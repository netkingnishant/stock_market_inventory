from django.urls import path

from . import views

urlpatterns = [
   path('signin/' ,views.signin, name='signin'),
   path('signup/' , views.signup),
   path('' , views.home, name='home'),
   path('logout/' , views.signout),
]