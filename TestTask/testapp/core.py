from django.db.models import Sum

from .models import Deal


def file_processing(csv_file):
    print(csv_file)
    file_data = csv_file.read().decode("utf-8")
    lines = file_data.split("\r\n")
    for line in lines:
        if line == '':
            break

        if line != lines[0]:
            fields = line.split(",")
            deal = Deal()
            deal.customer = fields[0]
            deal.item = fields[1]
            deal.total = fields[2]
            deal.quantity = fields[3]
            deal.date = fields[4]
            deal.save()


def get_queryset():
    clients_data = Deal.objects.all() \
        .values('customer') \
        .annotate(spent_money=Sum('total')) \
        .order_by('-spent_money')[:5]

    return clients_data
