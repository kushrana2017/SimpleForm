from django.contrib import admin
from django.urls import path, include

app_name = 'SimpleForm'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('Form.urls'))
]
