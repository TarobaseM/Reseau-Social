

from django.contrib import admin
from django.urls import path,include
from django.contrib.auth.views import LogoutView
from PostApp import views as postviews
from UsersApp import views as usersviews
# urls.py

from django.conf import settings
from django.conf.urls.static import static

from django.urls import path






urlpatterns = [
   
     path('administration/', admin.site.urls,name='administration'),
    path('', postviews.home, name='home'),
    
    path('home/', postviews.home, name='home'),
    path('poster/', postviews.poster, name='poster'),
    path('accounts/', include('allauth.urls')),
    path('login/', usersviews.google_login, name='login'),
    path('logout/', usersviews.google_logout, name='logout'),
    path('social/', include('allauth.socialaccount.urls')),
    path('post/<int:post_id>/like/', postviews.like_post, name='like_post'),


    
     ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
