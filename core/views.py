from django.views.generic import FormView

from django.urls import reverse_lazy

from django.contrib import messages

from .models import Servico, Portfolio, Colaborador

from .forms import ContatoForm

class IndexView(FormView):
    template_name = 'index.html'
    form_class = ContatoForm
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['servicos'] = Servico.objects.order_by('?').all
        context['portfolios'] = Portfolio.objects.order_by('?').all
        context['colaboradores'] = Colaborador.objects.order_by('?').all
        return context

    #Método para formulário válido
    def form_valid(self, form, *args, **kwargs):
        #Envia o e-mail
        form.send_mail()
        #Mensagem de sucesso
        messages.success(self.request, 'E-mail enviado com sucesso')
        return super(IndexView, self).form_valid(form, *args, **kwargs)

    # Método para formulário inválido
    def form_invalid(self, form, *args, **kwargs):
        # Mensagem de erro
        messages.error(self.request, 'Erro ao enviar e-mail')
        return super(IndexView, self).form_invalid(form, *args, **kwargs)