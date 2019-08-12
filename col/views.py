from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator


#
#
#
#
#
#
# def municipio(request):
#
#     if request.method == 'POST':
#         form = municipioForm(request.POST)
#         form2 = regionForm(request.POST)
#         #nombre = form['nombres'].value()
#
#         if form2.is_valid():
#             form2.save()
#
#         if form.is_valid():
#             form.save()
#     else:
#         formMun = municipioForm()
#         formReg = regionForm()
#
#     return render(request, 'formulario.html', {'municipio':formMun, 'region':regionForm})
#
#
#
#
#
#




from django.http import HttpResponse
from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy

from col.form import logicForm
from col.models import Municipio, Region


class MunicipioList(ListView):
    model = Municipio

class MunicipioView(DetailView):
    model = Municipio

class MunicipioCreate(CreateView):
    model = Municipio
    fields = ['name', 'code', 'is_active']
    success_url = reverse_lazy('municipio_list')

class MunicipioUpdate(UpdateView):
    model = Municipio
    fields = ['name', 'code', 'is_active']
    success_url = reverse_lazy('municipio_list')

class MunicipioDelete(DeleteView):
    model = Municipio
    success_url = reverse_lazy('municipio_list')




class RegionList(ListView):
    model = Region

class RegionView(DetailView):
    model = Region

class RegionCreate(CreateView):
    model = Region
    fields = ['name', 'code', 'municipios']
    success_url = reverse_lazy('region_list')

class RegionUpdate(UpdateView):
    model = Region
    fields = ['name', 'code', 'municipios']
    success_url = reverse_lazy('region_list')

class RegionDelete(DeleteView):
    model = Region
    success_url = reverse_lazy('region_list')



def numero(request):
    # if this is a POST request we need to process the form data
    if request.method == 'POST':
        # create a form instance and populate it with data from the request:
        form = logicForm(request.POST)
        # check whether it's valid:
        if form.is_valid():

            # process the data in form.cleaned_data as required
            # ...
            # redirect to a new URL:
            respuesta = form['numero'].value()
            respuesta=colnum_string(int(respuesta))
            return render(request, 'col/res.html', {'respuesta':respuesta})

    # if a GET (or any other method) we'll create a blank form
    else:
        form = logicForm()

    return render(request, 'col/logica.html', {'form': form})

def colnum_string(n):
    string = ""
    alfabeto = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'Ñ', 'O', 'P', 'Q', 'R', 'S','T', 'U', 'V', 'W', 'X', 'Y', 'Z']

    while n > 0:
        n, remainder = divmod(n - 1, len(alfabeto))
        print(n)
        print(remainder)
        print(alfabeto[remainder])
        string = alfabeto[remainder] + string
    return string

def prueba(request):
    return render(request, 'col/index.html')