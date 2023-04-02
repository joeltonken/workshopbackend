from django_filters.rest_framework import DjangoFilterBackend
from rest_framework.filters import OrderingFilter
from rest_framework import viewsets
from .models import Filme
from .serializers import FilmeSerializer
from rest_framework.authentication import SessionAuthentication
from rest_framework.permissions import IsAdminUser, IsAuthenticated, AllowAny

# Create your views here.
class FilmeViewSet(viewsets.ModelViewSet):
    queryset = Filme.objects.all()
    serializer_class = FilmeSerializer
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ['disponibilidade']
    ordering = ['ano']
    ordering_fields = [
        'ano',
        'titulo',
        'disponibilidade']
    authentication_classes = [SessionAuthentication]
    permission_classes = (IsAuthenticated, )