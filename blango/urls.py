from django.urls import path, include
import blog.views
import blango_auth.views

urlpatterns = [
    # other patterns
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", blango_auth.views.profile, name="profile"),
    path("", blog.views.index),
    path("api/v1/", include("blog.api_urls")),

]