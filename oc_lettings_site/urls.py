from django.contrib import admin
from django.urls import path

from oc_lettings_site import views as oc_lettings_site_views
from lettings import views as lettings_views
from profiles import views as profiles_views

urlpatterns = [
    path('', oc_lettings_site_views.index, name='index'),
    path('lettings/', lettings_views.index, name='lettings_index'),
    path('lettings/<int:letting_id>/', lettings_views.letting, name='letting'),
    path('profiles/', profiles_views.index, name='profiles_index'),
    path('profiles/<str:username>/', profiles_views.profile, name='profile'),
    path('admin/', admin.site.urls),
]
