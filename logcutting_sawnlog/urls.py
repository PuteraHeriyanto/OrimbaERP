
from django.urls import path, re_path
from  .import views



urlpatterns = [

    # The home page

    path('sawnlognew', views.SawnLogCreateView.as_view(), name='new-SawnLogData'),
    # path('', views.index, name='home'),
    # path('delete/<int:pk>/', views.delete, name='delete'),

    re_path(r'^sawnlog/(?:(?P<pk>[\w-]+)/)?(?:(?P<action>[^\d]+)/)?', views.SawnLogView.as_view(),
            name='sawnlog'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),
]

