from django.shortcuts import render
from django.views.generic import ListView, DetailView
from django.views.generic.dates import ArchiveIndexView, YearArchiveView, MonthArchiveView
from django.views.generic.dates import DayArchiveView, TodayArchiveView

from portfolio.models import Portfolio

from django.views.generic import FormView
from portfolio.forms import PortfolioSearchForm
from django.db.models import Q
# Create your views here.


#--- Detail View
class PortfolioDV(DetailView):
    model = Portfolio

#--- Archive View
class PortfolioAV(ArchiveIndexView):
    model = Portfolio
    date_field = 'modify_dt'

class PortfolioYAV(YearArchiveView):
    model = Portfolio
    date_field = 'modify_dt'
    make_object_list = True

class PortfolioMAV(MonthArchiveView):
    model = Portfolio
    date_field = 'modify_dt'

class PortfolioDAV(DayArchiveView):
    model = Portfolio
    date_field = 'modify_dt'

class PortfolioTAV(TodayArchiveView):
    model = Portfolio
    date_field = 'modify_dt'


#--- FormView
class SearchFormView(FormView):
    form_class = PortfolioSearchForm
    template_name = 'portfolio/portfolio.html'

    def form_valid(self, form):
        searchWord = form.cleaned_data['search_word']
        portfolio_list = Portfolio.objects.filter(Q(title__icontains=searchWord) | Q(description__icontains=searchWord) | Q(content__icontains=searchWord)).distinct()


        context = {}
        context['form'] = form
        context['search_term'] = searchWord
        context['object_list'] = portfolio_list

        return render(self.request, self.template_name, context)