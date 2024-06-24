from django.contrib import admin
from django.urls import path, include
from register import views as register_view
from django.contrib.auth import views as auth_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('dashboard.urls')),
    path('register/', register_view.register, name = 'user-register'),
    path('profile/', register_view.profile, name = 'user-profile'),
    path('', auth_views.LoginView.as_view(template_name = 'register/login.html'), name = 'user-login'),
    path('logout/', auth_views.LogoutView.as_view(template_name = 'register/logout.html'), name = 'user-logout'),
]
