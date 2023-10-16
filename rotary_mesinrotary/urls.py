
from django.urls import path, re_path
from  rotary_mesinrotary import views

urlpatterns = [

    # The home page

    path('mesinrotarynew', views.MesinRotaryCreateView.as_view(), name='new-MesinRotaryData'),
    path('', views.index, name='home'),

    re_path(r'^mesinrotary/(?:(?P<pk>[\w-]+)/)?(?:(?P<action>[^\d]+)/)?', views.MesinRotaryView.as_view(),
            name='mesinrotary'),

    # Matches any html file
    re_path(r'^.*\.*', views.pages, name='pages'),

]
