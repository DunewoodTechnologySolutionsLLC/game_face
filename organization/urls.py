from django.contrib import admin
from django.urls import path, include
from core import views as core_views
from organization import views as organization_views
from event import views as event_views

app_name = 'organization'
urlpatterns = [
    path('organization/', include(([
        path('', organization_views.OrganizationListView.as_view(), name='organization'),
        path('create/', organization_views.OrganizationCreateView.as_view(), name='create'),
        path('<organization_pk>/', include([
            path('', organization_views.OrganizationDetailView.as_view(), name='organization'),
            path('dashboard/', organization_views.OrganizationDashboardTemplateView.as_view(), name='dashboard'),
            path('building/', organization_views.OrganizationBuildingListView.as_view(), name='buildings'),
        ])),
    ], 'organization'), namespace='organization')),
    path('organization_building/', include(([
        path('create/', organization_views.OrganizationBuildingCreateView.as_view(), name='create'),
        path('<organization_building_pk>/', include([
            path('', organization_views.OrganizationBuildingDetailView.as_view(), name='organization_building'),
            path('dashboard/', organization_views.OrganizationBuildingDashboardTemplateView.as_view(), name='dashboard'),
            path('organization_event/', event_views.BuildingEventListView.as_view(), name='event'),
        ])),
    ], 'organization_building'), namespace='organization_building'))
]