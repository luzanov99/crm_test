from django.urls import include, path
from rest_framework.routers import DefaultRouter
from calendar_crm import views

router = DefaultRouter()

router.register('calendar', views.CalendarViewSet, basename='calendar')


app_name = 'calendar_snapt'

urlpatterns = [
    path('', include(router.urls)), 
]