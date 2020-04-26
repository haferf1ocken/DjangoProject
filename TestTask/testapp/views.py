from django.http import HttpResponse
from django.template import loader
from rest_framework import generics
from django.db.models import Count

from .core import *

from .serializers import *
from .models import Deal


def home(request):
    context = {}
    template = loader.get_template('testapp/index.html')
    if request.method == "POST":
        csv_file = request.FILES['deal_file']
        if not csv_file.name.endswith('.csv'):
            context['status'] = 'Error, Desc: File is not CSV type'
            return HttpResponse(template.render(context, request))
        Deal.objects.all().delete()
        file_processing(csv_file)
        context['status'] = 'Ok'
    else:
        clients = get_queryset()
        gems = Deal.objects.all().values('item').filter(customer__in=[client['customer'] for client in clients])\
            .distinct()
        print(gems)
        context['clients'] = clients
        context['gems'] = gems
    return HttpResponse(template.render(context, request))


class DealCreateView(generics.CreateAPIView):
    serializer_class = DealDetailSerializer


class DealListView(generics.ListAPIView):
    serializer_class = DealListSerializer
    queryset = Deal.objects.all()


class DealDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = DealDetailSerializer
    queryset = Deal.objects.all()