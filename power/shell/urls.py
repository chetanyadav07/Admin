
from django.urls import path
from.import views

urlpatterns = [
    path('',views.index),
    path('signup',views.signup,name='signup'),
    path('signin',views.signin,name='signin'),
    path('signuppage',views.signuppage,name='signuppage'),
    path('signinpage',views.signinpage,name='signinpage'),
    path('user',views.userhome,name='user'),
    path('logout',views.logout,name='logout')

]
