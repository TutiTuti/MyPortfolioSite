from django.shortcuts import render
from personalinfo.models import Grade
from personalinfo.utils import get_plot
# Create your views here.


def main_view(request):
    qs = Grade.objects.all()
    x = [x.grade for x in qs]
    y = [y.point for y in qs]
    chart = get_plot(x, y)
    return render(request, 'personalinfo/main.html', {'chat': chart})

