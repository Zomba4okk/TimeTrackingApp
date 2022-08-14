from django.urls import path

from apps.users.views import GetMyProfileView, SignInView, SignUpView


urlpatterns = [
    path("signin/", SignInView.as_view(), name="signin"),
    path("signup/", SignUpView.as_view(), name="signup"),
    path("profile/", GetMyProfileView.as_view(), name="get-my-profile"),
]
