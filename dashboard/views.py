from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from rest_framework import viewsets, mixins,response,permissions


class DashboardStatusViewset(viewsets.ViewSet):
    """
    list:
        返回Dashboard数据
    """
    permission_classes = (permissions.IsAuthenticated, )

    def list(self, request, *args, **kwargs):
        data = self.get_content_data()
        return response.Response(data)

    def get_content_data(self):
        return {
            "aa":11,
            "bb":22
        }