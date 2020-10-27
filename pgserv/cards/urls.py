from django.urls import path
from rest_framework.urlpatterns import format_suffix_patterns

from cards import views

urlpatterns = [
    path('', views.CardList.as_view()),
    path('<int:pk>/', views.CardDetail.as_view()),
    path('roll/', views.RollView.as_view()),
    path('claim/', views.ClaimView.as_view())
]


# urlpatterns = format_suffix_patterns(urlpatterns)