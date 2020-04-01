from django.urls import path
from . import views

app_name = 'paranuara'

urlpatterns = [
    path('api/company/<int:company_id>/employees/', views.EmployeesView.as_view({'get': 'list'}), name='company_employees'),
    path('api/company/<int:company_id>/add_employee/', views.EmployeesView.as_view({'post': 'create'}), name='add_employee'),
    path('api/mutual/<int:pk1>/<int:pk2>/', views.MutualFriendsView.as_view(), name='mutual_friends'),
    path('api/people/<int:pk1>/favourite_foods/', views.FavouriteFoodsView.as_view(), name='favourite_foods')
]