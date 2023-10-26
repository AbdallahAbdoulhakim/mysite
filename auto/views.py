from typing import Any
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from django.views.generic import View, ListView, DetailView, CreateView, UpdateView, DeleteView
from .models import Auto, Make
from django.urls import reverse_lazy
from django.contrib.auth.mixins import LoginRequiredMixin
from .forms import MakeForm
# Create your views here.

class AutoListView(ListView):
    model = Auto
    template_name="auto/auto_list.html"

    def get_context_data(self, **kwargs: Any):
        ctx = super().get_context_data(**kwargs)
        ctx["auto_count"] = Auto.objects.all().count()
        return ctx

class AutoDetailView(DetailView):
    model=Auto
    template_name="auto/auto_detail.html"


class AutoCreateView(LoginRequiredMixin, CreateView):
    model = Auto
    fields = "__all__"
    success_url = reverse_lazy('auto:auto_list')
    template_name = "auto/auto_form.html"

class AutoUpdateView(LoginRequiredMixin, UpdateView):
    model=Auto
    template_name="auto/auto_form.html"
    success_url=reverse_lazy('auto:auto_list')
    fields="__all__"

class AutoDeleteView(DeleteView):
    model = Auto
    template_name = "auto/auto_delete.html"
    success_url = reverse_lazy("auto:auto_list")


class MakeListView(View):
    def get(self, request):
        make_list = Make.objects.all()
        
        mk_list = [{"id": mk.id , "name":mk.name, "len":len(get_list_or_404(Auto, make=mk))} for mk in make_list]

        ctx = {"make_list": mk_list}

        return render(request, "auto/make_list.html", ctx)
    

class MakeCreateView(LoginRequiredMixin, View):
    def get(self,request):
        form = MakeForm()
        ctx = {"form":form}
        return render(request, "auto/make_form.html", ctx)

    def post(self, request):
        form = MakeForm(request.POST)

        if not form.is_valid():
            ctx = {"form":form}
            return render(request, "auto/make_form.html", ctx)
        
        form.save()

        return redirect(reverse_lazy("auto:make_list"))
        

class MakeDetailView(View):
    def get(self, request, pk):
        make = get_object_or_404(Make, pk=pk)

        ctx = {"make": make, "len":len(get_list_or_404(Auto, make=make))}

        return render(request, "auto/make_detail.html", ctx)


class MakeUpdateView(LoginRequiredMixin, View):
    def get(self,request, pk):
        make = get_object_or_404(Make, pk=pk)
        form = MakeForm(instance=make)
        ctx = {"form":form}
        return render(request, "auto/make_form.html", ctx)

    def post(self, request, pk):
        make = get_object_or_404(Make, pk=pk)
        form = MakeForm(request.POST, instance=make)

        if not form.is_valid():
            ctx = {"form":form}
            return render(request, "auto/make_form.html", ctx)
        
        form.save()

        return redirect(reverse_lazy("auto:make_list"))
        


class MakeDeleteView(LoginRequiredMixin, View):
    def get(self, request, pk):
        make = get_object_or_404(Make, pk=pk)
        ctx = {"make":make}
        return render(request, "auto/make_delete.html", ctx)
    
    def post(self, request, pk):
        make = get_object_or_404(Make, pk=pk)
        make.delete()
        return redirect(reverse_lazy("auto:make_list"))