from django.urls import path, include
from rest_framework import routers
from blog.views import BlogViewSet

# create a new router
router = routers.DefaultRouter()
# register our viewsets
router.register(r'blog', BlogViewSet) #register "/blog" routes


urlpatterns = [
    # add all of our router urls
    path("", include(router.urls))
]