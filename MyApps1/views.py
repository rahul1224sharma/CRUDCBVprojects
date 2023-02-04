from django.shortcuts import render
from MyApps1.models import Company
from django.views.generic import CreateView,ListView,DetailView,UpdateView,DeleteView
# Create your views here.
class Create(CreateView):
    model = Company
    fields = ('name','location','ceo')

class List(ListView):
    model = Company
                #companylist = Company.objects.all();
                #default template_name is company_list.html
                #defult context_object_name is company_list var
class Detail(DetailView):
    model = Company
                 # default template_name is company_detail.html
                 # defult context_object_name is "company"o r given-object for company_list, which is in usage for company_list.html

class Update(UpdateView):
    model = Company
    fields = ('name','ceo')

from django.urls import reverse_lazy
class Delete(DeleteView):
    model = Company
    success_url = reverse_lazy('companies')
