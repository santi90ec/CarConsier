from django.urls import path,include

urlpatterns = [
    path('', include('session.urls')),
    path('', include('catalogue.urls')),
    path('', include('transaction.urls'))
]




