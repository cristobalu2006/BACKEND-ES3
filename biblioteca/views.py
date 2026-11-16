from django.shortcuts import render

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response


from biblioteca.models import Autor, Libro
from biblioteca.serializers import AutorSerializer, LibroSerializer



@api_view(['POST', 'PUT'])
def crear_libro(request):
    libro_deserializado = LibroSerializer(data=request.data)

    if libro_deserializado.is_valid():
        libro_deserializado.save()

        return Response(libro_deserializado.data, status=status.HTTP_201_CREATED)
    else:
        return Response(libro_deserializado.errors, status=status.HTTP_400_BAD_REQUEST)




@api_view(['GET'])
def listar_libros(request):
    try:
        listado_libros = Libro.objects.all()
        serializado = LibroSerializer(listado_libros, many=True)

        return Response(serializado.data, status=status.HTTP_200_OK)
    except:
        return Response(status=status.HTTP_400_BAD_REQUEST)





@api_view(['PATCH'])
def modificar_libro(request, id):
    try:
        libro_obtenido = Libro.objects.get(id=id)
        serializado = LibroSerializer(libro_obtenido, data=request.data)

        if serializado.is_valid():
            serializado.save()

            return Response(status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_400_BAD_REQUEST)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)





@api_view(['DELETE'])
def eliminar_libro(request, id):
    try:
        libro_obtenido = Libro.objects.get(id=id)
        libro_obtenido.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)