from django import forms
from .models import TUser


def get_curators():
    curators = TUser.objects.all()
    curators_list = [(0, 'Все')]
    list_temp = [(x.id, x.name) for x in curators]
    curators_list.extend(list_temp)
    return curators_list


class CuratorForm(forms.Form):
    curator = forms.ChoiceField(label='Куратор', choices=get_curators, initial=0)

    def __init__(self, *args, **kwargs):
        super(CuratorForm, self).__init__(*args, **kwargs)
        for visible in self.visible_fields():
            visible.field.widget.attrs['class'] = 'form-control mx-sm-5'

    def clean_curator(self):
        pk = int(self.cleaned_data['curator'])
        if pk == 0:
            return pk
        try:
            curator = TUser.objects.get(pk=pk)
            return pk
        except TUser.DoesNotExist:
            raise forms.ValidationError('Invalid value', code='invalid')
