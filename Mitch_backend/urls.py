from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi


schema_view = get_schema_view(
    openapi.Info(
        title="Airtime Currency Exchange API\'s",
        default_version='v1',
        description="These API's are ment to be used in the build of an arduino+gsm Airtime - Currency exchange Market ",
        terms_of_service="https://www.mitch.com/policies/terms/",
        contact=openapi.Contact(email="mitch@gmail.com"),
        license=openapi.License(name="Open source License"),
    ),
    public=True,
)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('Exchange_rates/', include('exchange.urls')),
    path('transactions/', include('transactions.urls')),
    path('', schema_view.with_ui('swagger',
                                 cache_timeout=0), name='schema-swagger-ui'),

    path('api/api.json/', schema_view.without_ui(cache_timeout=0),
         name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc',
                                       cache_timeout=0), name='schema-redoc'),
]
