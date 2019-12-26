from django.contrib import admin
from django.urls import path, include

from core import views as core_views
from organization import views as organization_views
from event import views as event_views

app_name = 'core'
urlpatterns = [
    path('address/', include(([
        path('create/', core_views.AddressCreateView.as_view(), name='create'),
    ], 'address'), namespace='address')),
    path('state_province/', include(([
        path('create', core_views.StateProvinceCreateView.as_view(), name='create'),
    ], 'state_province'), namespace='state_province')),
    path('country/', include(([
        path('create', core_views.CountryCreateView.as_view(), name='create'),
    ], 'state_province'), namespace='state_province')),
]
