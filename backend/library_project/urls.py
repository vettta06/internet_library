from django.contrib import admin
from django.urls import include, path
from django.http import JsonResponse
from django.db import connection


def health_check(request):
    return JsonResponse({"status": "healthy", "service": "library"})


def render_ready(request):
    try:
        with connection.cursor() as cursor:
            cursor.execute("SELECT 1")
        return JsonResponse({"status": "ready"})
    except Exception as e:
        return JsonResponse({"status": "error", "message": str(e)}, status=500)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("library_app.urls")),
    path('health/', health_check, name='health_check'),
    path('ready/', render_ready, name='render_ready'),
]
