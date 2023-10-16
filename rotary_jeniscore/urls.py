
from django.urls import path, re_path
from  rotary_jeniscore import views

urlpatterns = [

    # The home page

    path('jeniscorenew', views.JenisCoreCreateView.as_view(), name='new-JenisCoreData'),
    # path('', views.index, name='home'),

    re_path(r'^jeniscore/(?:(?P<pk>[\w-]+)/)?(?:(?P<action>[^\d]+)/)?', views.JenisCoreView.as_view(),
            name='jeniscore'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
