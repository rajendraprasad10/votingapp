from django.urls import path
from .views import register, loginpage, logoutpage
# routes for all the login and register and logout pages
urlpatterns = [
    path('register/', register, name= 'register'),
    path('login/', loginpage, name = 'login'),
    path('logout', logoutpage, name='logout')
]