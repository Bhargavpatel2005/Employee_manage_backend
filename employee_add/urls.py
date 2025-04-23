from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import EmployeeViewSet, post_job,RegisterView,LoginView,adminviews,logoutview
from django.conf import settings
from django.conf.urls.static import static



router = DefaultRouter()
router.register(r'employee_add', EmployeeViewSet)
router.register(r'post_job', post_job)
urlpatterns = [
    path('', include(router.urls)),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('admin/', adminviews.as_view(), name='admin'),
    path('logout/', logoutview.as_view(), name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)