from django.contrib import admin
from django.conf  import settings
from django.urls import path, include
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('django.contrib.auth.urls')),


    path('', include('apps.core.urls')),
    path('empresas/', include('apps.empresas.urls')),
    path('documentos/', include('apps.documentos.urls')),
    path('funcionarios/', include('apps.funcionarios.urls')),
    path('departamentos/', include('apps.departamentos.urls')),
    path('horas-extras/', include('apps.registro_hora_extra.urls')),

] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # ver os arquivos em desenvolvimento 
