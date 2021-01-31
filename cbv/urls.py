from django.urls import path

from .views import CityListView, CityDetailView, CityCreateView, CityUpdateView
from .views import CityDeleteView, UserCreateView, LoginUserView, LogoutUserView

app_name = 'cbv'

urlpatterns = [
    path('main/', CityListView.as_view(), name='main'),
    path('create/', CityCreateView.as_view(), name='create'),
    path('detail/<int:pk>/', CityDetailView.as_view(), name='detail'),
    path('update/<int:pk>/', CityUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', CityDeleteView.as_view(), name='delete'),
    path('register/', UserCreateView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
]

# path('logout/', LogoutUserView.as_view(), name='logout'),
