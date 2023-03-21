from django.urls import path
from django.urls import re_path
from portfolio import views

app_name = 'portfolio'
urlpatterns = [


    # example /portfolio/archive/django-example/
    re_path(r'^portfolio/(?P<slug>[-\w]+)/$', views.PortfolioDV.as_view(), name='portfolio_detail'),

    # example /portfolio/archive/
    path('archive/', views.PortfolioAV.as_view(), name='portfolio_archive'),

    #example /portfolio/archive/2019/
    path('archive/<int:year>/', views.PortfolioYAV.as_view(), name='portfolio_year_archive'),

    #example /portfolio/archive/2019/nov/
    path('archive/<int:year>/<str:month>/', views.PortfolioMAV.as_view(), name='portfolio_month_archive'),

    #example /portfolio/archive/2019/nov/10/
    path('archive/<int:year>/<str:month>/<int:day>/', views.PortfolioDAV.as_view(), name='portfolio_day_archive'),

    #example /portfolio/archive/today/
    path('archive/today/', views.PortfolioTAV.as_view(), name='portfolio_today_archive'),

    #example : /portfolio/search/
    path('search/', views.SearchFormView.as_view(), name='search'),
]