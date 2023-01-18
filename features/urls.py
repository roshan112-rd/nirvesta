from django.urls import path,include
from . import views
from django.conf import settings
from django.views.static import serve
from django.urls import re_path
from django.conf.urls.static import static


urlpatterns = [
    path('', views.home, name="home"),
    path('about/', views.about, name="about"),
    path('team/', views.team, name="team"),
    
    path('services/', views.services, name="services"),
    path('login/', views.login, name="login"),
    path('blogs/', views.blogs, name="blogs"),
    path('contact/', views.contact, name="contact"),
    path('dashboard/', views.dashboard, name="dashboard"),
    path('logout/', views.logout, name="logout"),
    path('apply_loan/', views.apply_loan, name="apply_loan"),
    path('company_profile/', views.company_profile, name="company_profile"),
    path('shareholders/', views.shareholders, name="shareholders"),
    path('chat/', views.chat, name="chat"),
    path('mail/', views.mail, name="mail"),
    path('bulk_mail/', views.bulk_mail, name="bulk_mail"),
    path('selected_mail/', views.selected_mail, name="selected_mail"),
    path('service_detail/<int:id>', views.service_detail, name="service_detail"),
    path('blog_detail/<int:id>', views.blog_detail, name="blog_detail"),
    
    
    
    
    




    path('summernote/', include('django_summernote.urls')),
    re_path(r"^media/(?P<path>.*)$", serve, {"document_root": settings.MEDIA_ROOT}),
    re_path(r"^static/(?P<path>.*)$", serve, {"document_root": settings.STATIC_ROOT}),
]
