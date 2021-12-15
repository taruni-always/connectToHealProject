from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage, name = "Home Page"),
    path('home/', views.homepage, name = "Homepage"),
    path('about/', views.aboutpage, name = "about"),
    path('blogs/', views.viewBlogs, name = "Blog-Page"),
    path("registerUser/", views.registerUserPage, name="registerUser"),
    path("registerTherapist/", views.registerTherapistPage, name = " register2"),
    path("login/", views.loginPage, name="login"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()