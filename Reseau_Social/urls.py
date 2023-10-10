

from django.contrib import admin
from django.urls import path

from PostApp import views as postviews
from UsersApp import views as usersviews




urlpatterns = [
   
     path('admin/', admin.site.urls),
    path('', postviews.home, name='home'),
    path('login/', usersviews.login_view, name='login'),
    path('logout/', usersviews.LogoutView.as_view(), name='logout'),
    path('home/', postviews.home, name='home'),
    path('poster/', postviews.poster, name='poster'),]