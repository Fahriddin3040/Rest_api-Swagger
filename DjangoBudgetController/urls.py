from django.contrib import admin
from djangoBudget.views import *
from rest_framework import permissions, routers
from django.urls import path, include, re_path
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from djangoBudget.views import NoteAPIView


schema_view = get_schema_view(
   openapi.Info(
      title="API",
      default_version='v1',
   ),
   public=True,
)

router = routers.SimpleRouter()
router.register(r'note', NoteAPIView)
noteApi = NoteAPIView()

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls)),
    re_path(r'^swagger(?P<format>\.json|\.yaml<int:j>)$', schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(r'^swagger/$', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
]
