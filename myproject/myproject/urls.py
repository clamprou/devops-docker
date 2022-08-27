# awesome_website/urls.py

from django import views
from django.conf.urls import include, url
from django.contrib import admin
from users import views

urlpatterns = [
    url(r"^user/", include("users.urls")),
    url(r"^secretary/", include("secretary.urls")),
    url(r"^student/", include("students.urls")),
    url(r"^admin/", admin.site.urls),
    url("", views.dashboard, name='dashboard'),

]