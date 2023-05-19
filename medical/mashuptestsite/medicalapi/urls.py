from . import views
from django.urls import path




urlpatterns=[
    path('register',views.register,name="register_api"),
    path('login',views.login,name="login_api"),
    path('create',views.create,name="create_api"),
    path('edit',views.edit,name="edit_api"),
    path('delete',views.delete,name="delete"),
    path('logout',views.logout,name="logout_api")


]