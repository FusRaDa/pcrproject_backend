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

  path('reagents/', views.reagent_list_create_view, name='reagent_create_list'),
  path('reagents/<int:pk>/modify', views.reagent_retrieve_update_destroy, name='reagent_retrieve_update_destroy'),
 
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

]