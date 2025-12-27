from django.shortcuts import render, redirect, get_object_or_404
from .models import Pensionado, Trabajador
from .forms import PensionadoForm, TrabajadorForm


def index(request):
    return render(request, 'pensionados/index.html')


def pensiones(request):
    query = request.GET.get('q', '')
    form = PensionadoForm()
    error = False
    duplicate_error = False
    pensionados = Pensionado.objects.all()

    if query:
        pensionados = pensionados.filter(
            acreedor__icontains=query
        ) | pensionados.filter(
            nombre__icontains=query
        )

    if request.method == 'POST':
        form = PensionadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('pensiones')
        else:
            error = True
            if 'acreedor' in form.errors or 'nombre' in form.errors:
                duplicate_error = True

    return render(request, 'pensionados/pensiones.html', {
        'form': form,
        'pensionados': pensionados,
        'total_pensionados': pensionados.count(),
        'query': query,
        'error': error,
        'duplicate_error': duplicate_error
    })


def trabajadores(request):
    query = request.GET.get('q', '')
    form = TrabajadorForm()
    error = False
    duplicate_error = False
    trabajadores_list = Trabajador.objects.all()

    if query:
        trabajadores_list = trabajadores_list.filter(RPE__icontains=query) | trabajadores_list.filter(nombre__icontains=query)

    if request.method == 'POST':
        form = TrabajadorForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('trabajadores')
        else:
            error = True
            if 'RPE' in form.errors or 'nombre' in form.errors:
                duplicate_error = True

    return render(request, 'pensionados/trabajadores.html', {
        'form': form,
        'trabajadores': trabajadores_list,
        'total_trabajadores': trabajadores_list.count(),
        'query': query,
        'error': error,
        'duplicate_error': duplicate_error
    })


def editar_trabajador(request, pk=None):
    trabajador = None
    if pk:
        trabajador = get_object_or_404(Trabajador, pk=pk)

    if request.method == 'POST':
        form = TrabajadorForm(request.POST, instance=trabajador)
        if form.is_valid():
            form.save()
            return redirect('trabajadores')
    else:
        form = TrabajadorForm(instance=trabajador)

    return render(request, 'pensionados/editar_trabajador.html', {'form': form})


def eliminar_trabajador(request, pk):
    trabajador = get_object_or_404(Trabajador, pk=pk)
    if request.method == 'POST':
        trabajador.delete()
        return redirect('trabajadores')

    return render(request, 'pensionados/eliminar_trabajador.html', {
        'trabajador': trabajador
    })


def editar_pensionado(request, pk):
    pensionado = get_object_or_404(Pensionado, pk=pk)
    if request.method == 'POST':
        form = PensionadoForm(request.POST, instance=pensionado)
        if form.is_valid():
            form.save()
            return redirect('pensiones')
    else:
        form = PensionadoForm(instance=pensionado)

    return render(request, 'pensionados/editar_pensionado.html', {
        'form': form,
        'pensionado': pensionado
    })


def eliminar_pensionado(request, pk):
    pensionado = get_object_or_404(Pensionado, pk=pk)
    if request.method == 'POST':
        pensionado.delete()
        return redirect('pensiones')
    return redirect('pensiones')