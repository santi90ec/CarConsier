from django.urls import path     

from . import views
urlpatterns = [
    path('order_view', views.order_view),
    path('order_form', views.order_form),
    path('order_record', views.order_record),
    path('order_tracing_record', views.order_tracing_record),
    path('order_update', views.order_update),
    path('order_update_update', views.order_update_update),
    path('<int:number>/order_delete/', views.order_delete),
    path('<int:number>/order_edit/', views.order_edit),
    path('<int:number>/order_update/', views.order_edit_update)
]
