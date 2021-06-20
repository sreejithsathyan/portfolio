from django.urls import path
from .views import (
    company_detail_view,
    company_list_view,
    company_update_view,
    company_delete_view,
    company_create_view,
    )

urlpatterns = [
    path('', company_list_view),
    # path('/new', company_create_view),
    path('<str:slug>/', company_detail_view),
    path('<str:slug>/edit', company_update_view),
    path('<str:slug>/delete', company_delete_view),
]
