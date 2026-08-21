from django.urls import path
import blog.views
import blango_auth.views

urlpatterns = [
    # other patterns
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/profile/", blango_auth.views.profile, name="profile"),
    path("", blog.views.index)
]