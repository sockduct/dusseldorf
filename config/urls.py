"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
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
from django.conf import settings
from django.contrib import admin
from django.urls import include, path

if settings.ADMIN_SITE_URL_BASE == 'admin':
    ADMIN_URL = 'admin'
else:
    # Use secure/unique admin URL for production:
    ADMIN_URL = f'as-{settings.ADMIN_SITE_URL_BASE}'

urlpatterns = [
    # Django admin site:
    path(f'{ADMIN_URL}/', admin.site.urls),

    # User management:
    # path('accounts/', include('django.contrib.auth.urls')),
    # Replaced default with django-allauth:
    path('accounts/', include('allauth.urls')),

    # Local apps:
    # Replaced with django-allauth:
    # path('accounts/', include('accounts.urls')),
    path('paths/', include('paths.urls')),
    path('', include('pages.urls')),
    path('', include('posts.urls')),
]

if settings.DEBUG:
    import debug_toolbar

    urlpatterns += path('__debug__/', include(debug_toolbar.urls)),
