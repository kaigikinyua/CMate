from django.urls import path
from . import views
urlpatterns=[
        #default homepage
        path('',views.home,name='home'),
        path('login/',views.login,name="login"),
        path('signup/',views.signup,name="signup"),
    ]
