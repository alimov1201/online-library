from django.urls import path
from account.views import register_page, login_page, logout_function


urlpatterns = [
    path('register/', register_page, name='register'),
    path('login/', login_page, name='login'),
    path('logout/', logout_function, name='logout')
]