
from django.contrib import admin
from django.urls import path, re_path
from api import views as api_views
from user_view import views as user_views
urlpatterns = [
    re_path(r'^main', user_views.main),
    path('admin/', admin.site.urls),
]
