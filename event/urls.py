from django.contrib import admin
from django.urls import path, include

from event import views as event_views

app_name = 'event'
urlpatterns = [
    path('organization_event/<organization_event_pk>/$', event_views.OrganizationEventDetailView.as_view(), name='organization_event'),

]