from django.shortcuts import render
from rest_framework import permissions, viewsets, authentication
from .models import List, Item

from .serializers import ListSerializer,ItemSerializer


class ListViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    serializer_class = ListSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication, authentication.SessionAuthentication]

    def get_queryset(self):
        user = self.request.user
        return List.objects.filter(owner=user)


class ItemViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [permissions.IsAuthenticated]
    authentication_classes = [authentication.TokenAuthentication,authentication.SessionAuthentication]

