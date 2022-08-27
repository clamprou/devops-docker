from django.conf.urls import include, url
from secretary.views import makeApply

urlpatterns = [
    url(r"^makeApply/", makeApply, name="makeApply"),
]