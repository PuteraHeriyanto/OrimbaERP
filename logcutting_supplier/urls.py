
from django.urls import path, re_path
from  .import views

urlpatterns = [

    # The home page

    path('suppliernew', views.SupplierCreateView.as_view(), name='new-SupplierData'),
    # path('', views.index, name='home'),

    re_path(r'^supplier/(?:(?P<pk>[\w-]+)/)?(?:(?P<action>[^\d]+)/)?', views.SupplierView.as_view(),
            name='supplier'),

    # Matches any html file
    # re_path(r'^.*\.*', views.pages, name='pages'),

]
