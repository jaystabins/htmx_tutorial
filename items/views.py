from django.shortcuts import render
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView
from items.models import Item
from items.forms import ItemForm
from django.http import HttpResponse

def item_dashboard(request):
    return render(request, template_name='items/home.html')

class ItemListView(ListView):
    template_name = 'items/components/item_list.html'
    context_object_name = 'items'
    class Meta:
        model = Item

    def get_queryset(self):
        return Item.objects.all()
    
class ItemDetailView(DetailView):
    template_name = 'items/components/item_detail.html'
    class Meta:
        model = Item

    def get_queryset(self, queryset=None):
        return Item.objects.filter(pk=self.kwargs['pk'])

class ItemUpdateView(UpdateView):
    form_class = ItemForm
    template_name = 'items/components/update_item.html'
    class Meta:
        model = Item

    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Item.objects.filter(pk=pk)

    def form_valid(self, form):
        form.save()
        response = HttpResponse()
        response['HX-Trigger'] = 'item_list_updated'
        return response

class ItemDeleteView(DeleteView):
    template_name = 'items/components/delete_confirm.html'
    
    class Meta:
        model = Item
        
    def get_queryset(self):
        pk = self.kwargs.get('pk')
        return Item.objects.filter(pk=pk)

    def delete(self, request, *args, **kwargs):
        self.get_object().delete()
        response = HttpResponse()
        response['HX-Trigger'] = 'item_list_updated'
        return response

class ItemCreateView(CreateView):
    form_class = ItemForm
    template_name = 'items/components/add_item_form.html'

    class Meta:
        model = Item

    def form_valid(self, form):
        form.save()
        response = HttpResponse()
        response['HX-Trigger'] = 'item_list_updated'
        return response