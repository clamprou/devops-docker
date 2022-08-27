from django.conf.urls import include, url
from students.views import apply

urlpatterns = [
    url(r"^apply/", apply, name="apply"),
]