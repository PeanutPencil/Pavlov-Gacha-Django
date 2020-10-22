from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from cards import views

urlpatterns = [
    path('cards/', views.CardList.as_view()),
    path('cards/<int:pk>/', views.CardDetail.as_view()),
]


# urlpatterns = format_suffix_patterns(urlpatterns)