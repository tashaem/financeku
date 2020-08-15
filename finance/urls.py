from django.urls import path 

from . import views 

urlpatterns =[  
	path("", views.index, name="index"),
    path("register", views.register, name="register"),
    path("login", views.loginpage, name="loginpage"),
    path("logout", views.logoutpage, name="logoutpage"),
    path("categorize", views.categorize, name="categorize"),
    path("edit", views.edit, name="edit")
]
