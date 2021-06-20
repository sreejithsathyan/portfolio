from django import forms
from django.http import Http404
from django.shortcuts import get_object_or_404, render
from django.contrib.admin.views.decorators import staff_member_required
from .models import Company
# Create your views here.
from .forms import CompanyForm

# def company_detail_page(request,slug):
#     # obj = Company.objects.get(id=companys_id)
#     obj = get_object_or_404(Company ,slug=slug )
#     template_name = 'Company_name_Details.html'
#     context = {"object": obj}
#     return render(request,template_name,context)


# CRUD
@staff_member_required
def company_create_view(request):
    form = CompanyForm(request.POST or None)
    if form.is_valid():
        obj = Company.objects.create(**form.cleaned_data)
        form = CompanyForm()
    template_name = 'form.html'
    context = {"form": form}
    return render(request,template_name,context)


def company_list_view(request):
    qs = Company.objects.all()
    template_name = 'list.html'
    context = {"objectlist": qs}
    return render(request,template_name,context)

def company_detail_view(request,slug):
    # obj = Company.objects.get(id=companys_id)
    obj = get_object_or_404(Company ,slug=slug )
    template_name = 'detail.html'
    context = {"object": obj}
    return render(request,template_name,context)

def company_update_view(request,slug):
    obj = get_object_or_404(Company ,slug=slug )
    template_name = 'form.html'
    context = {"form": form}
    return render(request,template_name,context)

def company_delete_view(request):
    obj = get_object_or_404(Company ,slug=slug )
    template_name = 'delete.html'
    context = {"object": obj}
    return render(request,template_name,context)