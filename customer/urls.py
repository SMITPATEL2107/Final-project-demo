from django.urls import path,include    
from customer import  views 

urlpatterns = [
    path('',views.Main,name="mainpage"),
    path('register',views.Register,name="register"),
    path('login',views.Login,name="login"),
    path("registeruser",views.RegisterUser,name="registeruser"),
    path("loginuser",views.LoginUser,name="loginuser"),
    path("alldata/",views.AllData,name="alldata"), 
    path("logout/",views.Logout,name="logout"),
    path("update/",views.GetById,name="update")    
]   