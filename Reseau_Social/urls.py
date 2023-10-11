

from django.contrib import admin
from django.urls import path
from django.contrib.auth.views import LogoutView
from PostApp import views as postviews
from UsersApp import views as usersviews
# urls.py

from django.conf import settings
from django.conf.urls.static import static





urlpatterns = [
   
     path('admin/', admin.site.urls),
    path('', postviews.home, name='home'),
    path('login/', usersviews.login_view, name='login'),
    path('logout/', LogoutView.as_view(next_page='login'),name='logout'),
    path('home/', postviews.home, name='home'),
    path('poster/', postviews.poster, name='poster'),]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
