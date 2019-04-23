from django.urls import path
from .views import *
app_name = "bookmark"

urlpatterns = [
    path('', ListCardLV.as_view(), name='index'),
    path('list/', ListCardLV.as_view(), name='list_show'),
    path('list/add/', ListCreateView.as_view(), name='list_add'),
    path('list/<int:pk>/update/', ListUpdateView.as_view(), name='list_update'),
    path('list/<int:pk>/delete/', ListDeleteView.as_view(), name='list_delete'),
    path('card/add/', CardCreateView.as_view(), name='card_add'),
    path('card/<int:pk>/update', CardUpdateView.as_view(), name='card_update'),
    path('card/<int:pk>/delete', CardDeleteView.as_view(), name='card_delete'),
]
