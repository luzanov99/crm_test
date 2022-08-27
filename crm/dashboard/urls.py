from django.urls import include, path
from rest_framework.routers import DefaultRouter
from dashboard import views

router = DefaultRouter()

router.register('metrics', views.DashboardMetrics, basename='metrics')


app_name = 'dashboard'

urlpatterns = [
    path('', include(router.urls)), 
]