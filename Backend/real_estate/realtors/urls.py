from django.urls import path
from .views  import RealtorListView,RealtorView,TopSellerView



urlpatterns = [
    path('', RealtorView.as_view()),
    path('topseller',TopSellerView.as_view()),
    path('<pk>', RealtorListView.as_view()),
]
