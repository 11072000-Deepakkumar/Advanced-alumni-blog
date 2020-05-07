"""alumni_sys URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from alumni import views as alumni_views 
from django.conf import settings 
from django.conf.urls.static import static

#Login and Logout built in views!
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('prolist/',alumni_views.list_view.as_view(),name='prolistview'),
    path('prodetails/<int:project_id>',alumni_views.detail_view,name='prodetails'),
    path('register',alumni_views.Register,name='register'),
    path('login',auth_views.LoginView.as_view(template_name='alumni/login.html'),name='login'),
    path('logout',auth_views.LogoutView.as_view(template_name='alumni/logout.html'),name='logout'),
    
    path('promentor/<int:project_id>',alumni_views.mentor_view,name='mentors'),
    path('procreate',alumni_views.create_view,name='procreate'),
    path('proupdate/<int:pk>',alumni_views.update_view.as_view(),name='proupdate'),
    path('prodelete/<int:pk>',alumni_views.DeleteView.as_view(),name='prodelete'),
    path('author/<int:project_id>',alumni_views.author_view,name='proauthor'),

    #Profile Views 
    path('profile',alumni_views.profile,name='profile'),
    path('profilelist',alumni_views.profilelist.as_view(),name='profilelist'),
    path('profiledetails/<int:pk>',alumni_views.profileldetailsview.as_view(),name='profiledetails'),
    path('password-reset/',
         auth_views.PasswordResetView.as_view(
             template_name='alumni/password_reset.html'
         ),
         name='password_reset'),
    path('password-reset/done/',
         auth_views.PasswordResetDoneView.as_view(
             template_name='alumni/password_reset_done.html'
         ),
         name='password_reset_done'),
    path('password-reset-confirm/<uidb64>/<token>/',
         auth_views.PasswordResetConfirmView.as_view(
             template_name='alumni/password_reset_confirm.html'
         ),
         name='password_reset_confirm'),
    path('password-reset-complete/',
         auth_views.PasswordResetCompleteView.as_view(
             template_name='alumni/password_reset_complete.html'
         ),
         name='password_reset_complete'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
