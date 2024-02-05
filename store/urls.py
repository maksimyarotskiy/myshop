from django.conf.urls.static import static
from django.urls import path, re_path
from config import settings
from . import views

urlpatterns = [
    path('home/', views.HomeView.as_view(), name='home'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
