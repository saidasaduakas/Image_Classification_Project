from django.contrib import admin
import django
from django.urls import path
from django.urls import re_path as url
from firstapp import views
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
    path('admin/', admin.site.urls),
    url('^$', views.index, name="homepage"),
    url('predictImage', views.predictImage, name="predictImage"),
    url('viewDataBase', views.viewDataBase, name="viewDataBase"),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)