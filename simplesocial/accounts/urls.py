from django.conf.urls import url
from django.contrib.auth import views as auth_views
from . import views
from django.urls import path
app_name = 'accounts'

urlpatterns = [
    url(r"login/$", auth_views.LoginView.as_view(template_name="accounts/login.html"),name='login'),
    url(r"logout/$", auth_views.LogoutView.as_view(), name="logout"),
    url(r"signup/$", views.SignUp.as_view(), name="signup"),
    

    path(r"profile/(?P<slug>[-\w]+)/", views.profile.as_view(), name = "profile"),
    #path(r"update/<int:pk>", views.Editprofile.as_view(), ),
    url(r"^update/(?P<slug>[-\w]+)/$",views.Editprofile.as_view(), name="update"),
]
