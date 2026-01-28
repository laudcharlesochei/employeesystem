from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    # Built-in auth views: /login/, /logout/, /password_change/, ...
    path('', include('django.contrib.auth.urls')),
    # App routes (home, about, employees CRUD)
    path('', include('employees.urls')),
]
