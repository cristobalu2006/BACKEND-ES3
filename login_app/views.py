from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from django.contrib.auth import authenticate
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework.response import Response

# Create your views here.

@api_view(['POST'])
@permission_classes([AllowAny])
def login(request):
    #obtiene username y password desde el frontend (json)

    usuario  = request.data.get('username')
    password = request.data.get('password')

    #validación

    if not usuario or not password:
        return Response(
            {'error': 'Se requieren usuario y contraseña'},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    user = authenticate(username=usuario, password = password)

    if user is not None:
        token, created = Token.objects.get_or_create(user=user)

        return {
                'token':token.key,
                'usuario': user.username,
                'user_id': user.id}

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def logout(request):
    pass