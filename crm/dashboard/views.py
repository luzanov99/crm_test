from re import template
from django.shortcuts import render
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from dashboard.metrics import get_report
from dashboard.models import Metrics
from dashboard.serializers import MetricsSerializer
import json
class DashboardMetrics(ModelViewSet):
    
    serializer_class = MetricsSerializer
    
   
    #http://127.0.0.1:8000/dashboard/metrics/?start_date=2022-03-23&end_date=2022-03-23
    def list(self, request):
        start_date=request.GET.get("start_date", "")
        end_date=request.GET.get("end_date", "")
        metric=get_report(start_date, end_date)
        result=json.dumps(metric.request)
        return Response(result, status=status.HTTP_200_OK)