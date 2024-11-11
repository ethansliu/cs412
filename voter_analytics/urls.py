from django.urls import path
from django.conf import settings
from . import views

urlpatterns = [ 
    path(r'', views.AllVotersView.as_view(), name="voters"),
    path(r'voter/<int:pk>', views.DetailVoterView.as_view(), name="detail_voter"),
    path(r'graphs', views.GraphView.as_view(), name="graphs"),
]