
from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from classes import views
from api_app import api_views
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    path('classrooms/', views.classroom_list, name='classroom-list'),
    path('classrooms/<int:classroom_id>/', views.classroom_detail, name='classroom-detail'),

    path('classrooms/create', views.classroom_create, name='classroom-create'),
    path('classrooms/<int:classroom_id>/update/', views.classroom_update, name='classroom-update'),
    path('classrooms/<int:classroom_id>/delete/', views.classroom_delete, name='classroom-delete'),

    path('api/token/', TokenObtainPairView.as_view(), name='api-login'),
    path('api/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('classroomlist/', api_views.APIListView.as_view(), name="api-classroom-list"),
    path('classroom/<int:classroom_id>/', api_views.classroomDetails.as_view(), name="api-classroom-detail"),
    path('classroom/<int:classroom_id>/update/', api_views.UpdateClassroom.as_view(), name="api-classroom-update"),
    path('classroom/<int:classroom_id>/cancel/', api_views.CancelClassroom.as_view(), name="api-classroom-delete"),
    path('classroom/', api_views.classroomCreate.as_view(), name="api-classroom-create"),
    #path('Register/', api_views.UserCreateAPIView.as_view(), name="register"),


]

if settings.DEBUG:
	urlpatterns+=static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
	urlpatterns+=static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
