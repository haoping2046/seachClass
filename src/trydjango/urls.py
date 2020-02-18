"""trydjango URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
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
from django.urls import path

from pages.views import *
from products.views import *
from policy.views import *

urlpatterns = [
    path('', course_view, name='course'),
    path('course/', course_view, name='course'),
    path('plan/', plan_view, name='plan'),
    path('mepolicy/', ME_policy_view, name='mepolicy'),
    path('mspolicy/', MS_policy_view, name='mspolicy'),

    path('home/', home_view, name='home'),
    path('admin/', admin.site.urls),
    path('product/', product_detail_view),
    # path('create/', product_create_view),
    path('initial/', render_initial_data),

    path('weather/', product_create_view)
]
