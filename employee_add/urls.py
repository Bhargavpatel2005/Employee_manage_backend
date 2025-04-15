from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, post_job
from django.conf import settings
from django.conf.urls.static import static


router = DefaultRouter()
router.register(r'employee_add', EmployeeViewSet)
router.register(r'post_job', post_job)

urlpatterns = [
    path('', include(router.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)