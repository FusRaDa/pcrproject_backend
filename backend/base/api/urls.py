from django.urls import path
from . import views
from .views import MyTokenObtainPairView

from rest_framework_simplejwt.views import (
  TokenRefreshView
)

urlpatterns = [
  path('', views.getRoutes),
  path('token/', MyTokenObtainPairView.as_view(), name='token_obtain_pair'),
  path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

  path('reagents/', views.reagent_list_view, name='reagent_list'),
  path('reagents/create/', views.reagent_create_view, name='reagent_create'),
  path('reagent/<int:pk>/retrieve/', views.reagent_retrieve_view, name="reagent_retrieve"),
  path('reagent/<int:pk>/update/', views.reagent_update_view, name="reagent_update"),
  path('reagent/<int:pk>/destroy/', views.reagent_destroy_view, name="reagent_destroy"),

  path('supplies/', views.supply_list_view, name='supply_list'),
  path('supllies/create/', views.supply_create_view, name='supply_create'),
  path('supplies/<int:pk>/retrieve/', views.supply_retrieve_view, name='supply_retrieve'),
  path('supplies/<int:pk>/update/', views.supply_update_view, name='supply_update'),
  path('supplies/<int:pk>/destroy/', views.supply_destroy_view, name='supply_destroy'),
 
  path('assays/', views.assay_list_view, name='assay_list'),
  path('assays/create/', views.assay_create_view, name='assay_create'),
  path('assays/<int:pk>/retrieve/', views.assay_retrieve_view, name='assay_retrieve'),
  path('assays/<int:pk>/update/', views.assay_update_view, name='assay_update'),
  path('assays/<int:pk>/destroy/', views.assay_destroy_view, name='assay_destroy'),

  path('batches/', views.batch_list_view, name='batch_list'),
  path('batches/create/', views.batch_create_view, name='batch_create'),
  path('batches/<int:pk>/retrieve/', views.batch_retrieve_view, name='batch_retrieve'),
  path('batches/<int:pk>/update/', views.batch_update_view, name='batch_update'),
  path('batches/<int:pk>/destroy/', views.batch_destroy_view, name='batch_destroy'),

  path('labels/', views.label_list_view, name='label_list'),
  path('labels/create/', views.label_create_view, name='label_create'),
  path('labels/<int:pk>/retrieve/', views.label_retrieve_view, name='label_retrieve'),
  path('labels/<int:pk>/update/', views.label_update_view, name='label_update'),
  path('labels/<int:pk>/destroy/', views.label_destroy_view, name='label_destroy'),
  
]