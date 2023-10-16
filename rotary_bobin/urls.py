
from django.urls import path, re_path
from  rotary_bobin import views

urlpatterns = [

    # The home page

    path('bobinnew', views.BobinCreateView.as_view(), name='new-BobinData'),
    # path('', views.index, name='home'),

    re_path(r'^bobin/(?:(?P<pk>[\w-]+)/)?(?:(?P<action>[^\d]+)/)?', views.BobinView.as_view(),
            name='bobin'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
