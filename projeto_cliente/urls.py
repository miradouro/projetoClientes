from django.contrib import admin
from django.urls import path
from .views import hello, articles

urlpatterns = [
    path('hello/', hello),
    path('articles/<int:year>', articles),
    path('admin/', admin.site.urls),
]
