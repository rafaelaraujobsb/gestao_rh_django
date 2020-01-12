from django.urls import path

# from .views import home,
from .views import DocumentoCreate

urlpatterns = [
    path('novo/<int:funcionario_id>', DocumentoCreate.as_view(), name='create_documento'),
    # path('editar/<int:pk>', FuncionarioEdit.as_view(), name='update_funcionario'),
    # path('delete/<int:pk>', FuncionarioDelete.as_view(), name='delete_funcionario'),
]
