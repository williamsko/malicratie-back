"""playoff URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from django.conf.urls import url, include

from django.conf.urls import url, include
from tastypie.api import Api


from publication.api.resources import PublicationsResource, CategoryResource
from base.api.resources import PartnersResource, AboutResource
from project.api.resources import  ProjectResource, SearchResource, GeoResource as GResource
from project.api.denonciation import DenonciationResource
from project.api.comments import CommentsResource
from event.api.resources import  EventResource
from geo.api.resources import PDECSResource, GeoResource

v1_api = Api(api_name='v1')
v1_api.register(CategoryResource())
v1_api.register(PublicationsResource())
v1_api.register(PartnersResource())
v1_api.register(EventResource())
v1_api.register(ProjectResource())
v1_api.register(AboutResource())
v1_api.register(SearchResource())
v1_api.register(DenonciationResource())
v1_api.register(CommentsResource())
v1_api.register(GeoResource())
v1_api.register(PDECSResource())
v1_api.register(GResource())



urlpatterns = [
    path('admin/', admin.site.urls),
]


urlpatterns += [

    url(r'^endpoints/', include(v1_api.urls)),

]

from django.conf.urls.static import static
from django.conf import settings

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

urlpatterns += [
    # ... the rest of your URLconf goes here ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.site_header = "Malicratie Admin"
admin.site.site_title = "Malicratie Admin"
admin.site.index_title = "Plateforme administration'"
