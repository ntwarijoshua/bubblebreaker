from django.shortcuts import render
from rest_framework import viewsets
from .models import SystemAdmin
from .serializers import SystemAdminSerializer
from rest_framework.permissions import IsAuthenticated


class SystemAdminViewSet(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    queryset = SystemAdmin.objects.all()
    serializer_class = SystemAdminSerializer
