from django.urls import path
from . import views
urlpatterns=[
        #default homepage
        path('',views.home,name='home'),
        path('login/',views.login,name="login"),
        path('signup/',views.signup,name="signup"),
        path(r'^addFriend/(?P<friend>\w+)/',views.addFriend,name="addFriend"),
    ]
