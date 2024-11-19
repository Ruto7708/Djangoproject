"""
URL configuration for portfolio2 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include

from company import views
from company.views import resume_view

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.home_view, name='index'),
    path('about/', views.about, name='about'),
    path('contact/', views.contact_view, name='contact'),
    path('services/', views.services, name='services'),
    path('portfolio/', views.portfolio, name='portfolio'),
    path('portfolio_details/', views.portfolio_details, name='portfolio_details'),
    # path('resume', views.resume, name='resume'),
   path('resume',views.resume_view, name='resume'),

]



