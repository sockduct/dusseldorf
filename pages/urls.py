from django.urls import path

from .views import (
    AboutPageView,
    ContactPageView,
    ErrorPageView,
    LeaderboardPageView,
    SuccessPageView
)

urlpatterns = [
    path('about/', AboutPageView.as_view(), name='about'),
    path('contact/', ContactPageView.as_view(), name='contact'),
    path('error/', ErrorPageView.as_view(), name='error'),
    path('success/', SuccessPageView.as_view(), name='success'),
    path('leaderboard/', LeaderboardPageView.as_view(), name='leaderboard'),
]
