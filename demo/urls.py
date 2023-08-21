from django.contrib import admin
from django.urls import path, include  # Don't forget to import include!

urlpatterns = [
    path('admin/', admin.site.urls),
    path('todo/', include('task.urls')),  # Include the app's URLs here
]
