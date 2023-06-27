from django.contrib import admin
from django.urls import path, include
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

schema_view = get_schema_view(
    openapi.Info(
        title="Bleswa APIs",
        default_version='v1',
        description="Bleswa APIs",
        terms_of_service="https://www.ourapp.com/policies/terms/",
        contact=openapi.Contact(email="contact@beezhut.com"),
        license=openapi.License(name="Test License"),
    ),
    public=True
)

admin.site.site_header = 'Bleswa Solutions'                    
admin.site.index_title = 'Site Administration'           
admin.site.site_title = 'Bleswa Solutions'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include('core.urls')),

    path('', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('api/api.json/', schema_view.without_ui(cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
