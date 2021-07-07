from django.shortcuts import render
from django.views.generic.edit import FormView
from django.urls import reverse_lazy
from .forms import CuratorForm
from .models import TProcedures

# Create your views here.


class MyBaseView(FormView):
    form_class = CuratorForm
    template_name = 'base.html'
    success_url = reverse_lazy('web_app:index')
    t_user = 0

    def get(self, request, *args, **kwargs):
        if request.GET.get('t_user'):
            self.t_user = int(request.GET.get('t_user'))
        return super(MyBaseView, self).get(request, *args, **kwargs)

    def get_success_url(self):
        if self.t_user:
            return '{}?t_user={}'.format(super(MyBaseView, self).get_success_url(), self.t_user)
        else:
            return super(MyBaseView, self).get_success_url()

    def get_initial(self):
        if self.t_user:
            initial = {'curator': self.t_user}
            return initial
        else:
            return super(MyBaseView, self).get_initial()

    def form_valid(self, form):
        self.t_user = form.cleaned_data['curator']
        return super(MyBaseView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(MyBaseView, self).get_context_data(**kwargs)
        if self.t_user:
            t_procedures = TProcedures.objects.filter(curator__id=self.t_user)
        else:
            t_procedures = TProcedures.objects.all()
        context['data_x'] = [x.doc_publish_date_str for x in t_procedures]
        context['data_y'] = [y.max_price for y in t_procedures]
        return context

