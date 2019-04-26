from django.urls import path
from .views import *

app_name = "workmanagement"

urlpatterns = [
    path('', ListCardLV.as_view(), name='index'),
    path('worklist/', ListCardLV.as_view(), name='worklist_show'),
    path('worklist/add/', ListCreateView.as_view(), name='worklist_add'),
    path('worklist/<int:pk>/update/', ListUpdateView.as_view(), name='worklist_update'),
    path('worklist/<int:pk>/delete/', ListDeleteView.as_view(), name='worklist_delete'),
    path('card/<int:fk>/add/', CardCreateView.as_view(), name='card_add'),
    path('card/<int:fk>/<int:pk>/update/', CardUpdateView.as_view(), name='card_update'),
    path('card/<int:fk>/<int:pk>/delete/', CardDeleteView.as_view(), name='card_delete'),
]
