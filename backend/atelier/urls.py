
from multiprocessing.context import DefaultContext
from django.db import router
from django.urls import path,include
from .views import *
from atelier import views
from rest_framework.routers import DefaultRouter

# router = DefaultRouter()
# router.register('atelier',AtelierViews)
# router.register('client',ClientViews)
# router.register('consultant',ConsultantViews)

urlpatterns = [
    path('atelier/',views.AtelierViews.as_view({
    'get': 'list',
    'post': 'create'
})),
    path('client/',views.ClientViews.as_view({
    'get': 'list',
    'post': 'create'
})),
    path('consultant/',views.ConsultantViews.as_view({'get': 'list',
    'post': 'create'})),
]

