from django.contrib import admin
from django.urls import path


from biblioteca.views import crear_libro, listar_libros, modificar_libro, eliminar_libro
from login_app.views import login

urlpatterns = [
    path('admin/', admin.site.urls),

    path('/login', login),

    path('libro/crear', crear_libro),
    path('libros', listar_libros),
    path('libro/modificar/<int:id>', modificar_libro),
    path('libro/eliminar/<int:id>', eliminar_libro),
]