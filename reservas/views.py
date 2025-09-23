from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from .models import Reserva
from .forms import ReservaForm # Vamos criar este form

class ReservaListView(ListView):
    model = Reserva
    template_name = 'reservas/lista.html'
    context_object_name = 'reservas'

class ReservaCreateView(CreateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas/formulario.html'
    success_url = reverse_lazy('reservas:lista')

class ReservaUpdateView(UpdateView):
    model = Reserva
    form_class = ReservaForm
    template_name = 'reservas/formulario.html'
    success_url = reverse_lazy('reservas:lista')

class ReservaDeleteView(DeleteView):
    model = Reserva
    template_name = 'reservas/confirmar_delete.html'
    success_url = reverse_lazy('reservas:lista')