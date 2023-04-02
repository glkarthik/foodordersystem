from django.views import generic

from inventories.models import Inventory


# Create your views here.
class IndexView(generic.ListView):
    template_name = 'index.html'
    context_object_name = 'inventory_list'

    def get_queryset(self):
        return Inventory.objects.filter(qty__gte=1).order_by('-created')
