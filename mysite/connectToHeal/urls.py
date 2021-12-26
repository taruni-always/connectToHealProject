from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    path('', views.homepage, name = "Home Page"),
    path('home/', views.homepage, name = "Homepage"),
    path('userhome/', views.userhomepage, name = "userhome"),
    path('therapisthome/', views.therapisthomepage, name = "therapisthome"),
    path('discussion/', views.discussionPage, name = "dicussion"),
    path('about/', views.aboutpage, name = "about"),
    path('blogs/', views.viewBlogs, name = "blogs"),
    path('therapists/', views.viewTherapists, name = "therapists"),
    path('therapists/booksession', views.bookSession, name = "booksession"),
    path("registerUser/", views.registerUserPage, name="registerUser"),
    path("loginPage/", views.loginPage, name="loginPage"),
    path("logout/", views.logoutUser, name = "logout"),
] + static(settings.MEDIA_URL, document_root = settings.MEDIA_ROOT)

urlpatterns += staticfiles_urlpatterns()