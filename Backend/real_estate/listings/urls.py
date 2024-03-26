from django.urls import path
from .views import ListingView, ListingDetail, SearchView

urlpatterns = [
    path('listings/', ListingView.as_view(), name='listing-list'),
    path('listings/<slug:slug>/', ListingDetail.as_view(), name='listing-detail'),
    path('search/', SearchView.as_view(), name='listing-search'),
]
