
from django.contrib import admin
from django.urls import path,include
from app import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('StudentApi/',views.LCStudentApi.as_view(), name='api1'),
    # path('StudentApi/<int:pk>/', views.StudentApi.as_view(), name='api2')
]
