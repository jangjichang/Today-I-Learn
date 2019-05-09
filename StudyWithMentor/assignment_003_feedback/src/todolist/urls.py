from django.urls import path
from .views import *

app_name = "todolist"

urlpatterns = [
    path('', WorkCardLV.as_view(), name='index'),
    path('work/', WorkCardLV.as_view(), name='work_list'),
    path('work/add/', WorkCreateView.as_view(), name='work_add'),
    path('work/<int:pk>/update/', WorkUpdateView.as_view(), name='work_update'),
    path('work/<int:pk>/delete/', WorkDeleteView.as_view(), name='work_delete'),
    path('work/<int:pk>/complete/'. WorkCompleteView.as_view(), name='work_complete'),
    path('card/<int:fk>/add/', CardCreateView.as_view(), name='card_add'),
    path('card/<int:fk>/<int:pk>/update/', CardUpdateView.as_view(), name='card_update'),
    path('card/<int:fk>/<int:pk>/delete/', CardDeleteView.as_view(), name='card_delete'),
    # ToDo: Activity url settings
    # path('activity/<int:fk>/add/', ActivityCreateView.as_view(), name='card_add'),
    # path('activity/<int:fk>/<int:pk>/update/', ActivityUpdateView.as_view(), name='card_update'),
    # path('activity/<int:fk>/<int:pk>/delete/', ActivityDeleteView.as_view(), name='card_delete'),
]
