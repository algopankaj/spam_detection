# api/urls.py

from django.urls import path
from .views import UserRegistration, PhoneNumberSpamView, SearchUserView

urlpatterns = [
    path('register/', UserRegistration.as_view(), name='user-registration'),
    path('mark-spam/', PhoneNumberSpamView.as_view(), name='mark-spam'),
    path('search/', SearchUserView.as_view(), name='search-users'),
]
