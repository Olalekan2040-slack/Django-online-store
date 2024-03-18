from django.urls import path
from django.contrib.auth import views as auth_views
from django.urls import reverse_lazy
from . import views
from . forms import LoginForm
from django.contrib.auth.views import LogoutView
app_name = 'core'

urlpatterns =[
    path('', views.index, name='index'),
    path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('login/', auth_views.LoginView.as_view(template_name = 'core/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', LogoutView.as_view(next_page=reverse_lazy('core:login')), name='logout'),

    ]