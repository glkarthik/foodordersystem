import datetime

from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.urls import reverse

from orders.models import Order


# Create your views here.
def OrderView(request, order_id):
    order_data = get_object_or_404(Order, pk=order_id)
    return render(request, 'order_details.html', {'order_data': order_data})


def OrderSubmit(request):
    raw_data = request.POST.copy()
    del raw_data["csrfmiddlewaretoken"]
    order_date = datetime.datetime.strptime(raw_data.pop("order_date")[0], "%d/%m/%Y").date()
    item_ids = [k for k,v in raw_data.items() if v == 'true']
    new_order = Order.objects.create(date=order_date)
    new_order.items.add(*item_ids)
    return HttpResponseRedirect(reverse('orders:order', args=(new_order.id,)))
