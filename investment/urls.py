from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^home/', views.home, name='home'),
    url(r'^create/', views.create, name='create_portfolo'),
    url(r'details/(?P<invest_id>\d+)/$', views.details, name='invest_details'),
    url(r'^export-to-excel/', views.export_to_excel, name='export_to_excel'),
]
