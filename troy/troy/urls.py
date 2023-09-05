
from django.contrib import admin
from django.urls import path ,include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include('cleaning.urls')),

]+static(settings.MAIN_TAMPLATE_URL, document_root=settings.MAIN_TAMPLATE_ROOT)
