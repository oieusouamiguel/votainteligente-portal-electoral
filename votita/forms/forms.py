# coding=utf-8
from django import forms
from collections import OrderedDict
from popular_proposal.forms.forms import get_possible_generating_areas
from django.utils.translation import ugettext as _
from votita.models import KidsGathering
from django.forms import ModelForm


class CreateGatheringForm(ModelForm):
    class Meta:
        model = KidsGathering
        fields = ['name', 'presidents_features']

    def __init__(self, *args, **kwargs):
        self.proposer = kwargs.pop('proposer')
        super(CreateGatheringForm, self).__init__(*args, **kwargs)

    def save(self):
        instance = super(CreateGatheringForm, self).save(commit=False)
        instance.proposer = self.proposer
        instance.save()
        return instance



class UpdateGatheringForm(ModelForm):
    male = forms.IntegerField(label = "# Hombres",
                              min_value = 0,
                              initial=0)
    female = forms.IntegerField(label = "# Mujeres",
                                min_value = 0,
                                initial=0)
    others = forms.IntegerField(label = "# Otros",
                                min_value = 0,
                                initial=0)
    class Meta:
        model = KidsGathering
        fields = ['image']

    def clean(self):
        cleaned_data = super(UpdateGatheringForm, self).clean()
        base_fields = [field.name for field in self._meta.model._meta.get_fields()]
        stats_data = {}
        for key  in cleaned_data.keys():
            if key not in base_fields:
                stats_data[key] = cleaned_data.pop(key)
        cleaned_data['stats_data'] = stats_data
        return cleaned_data

    def save(self):
        instance = super(UpdateGatheringForm, self).save(commit=False)
        instance.stats_data = self.cleaned_data['stats_data']
        instance.save()
        return instance

TOPIC_CHOICES = (('', u'Selecciona una categoría'),
                 ('proteccion_y_familia', u'Protección y familia'),
                 ('educacion_y_trabajo', u'Educación y trabajo'),
                 ('tecnologia', u'Tecnología y comunicaciones'),
                 ('diversidad', u'Diversidad e integración'),
                 ('cultura', u'Cultura y tiempo libre'),
                 ('medio_ambiente', u'Medio ambiente'),
                 ('salud', u'Salud y bienestar'),
                 ('politica', u'Política y participación'),
                 )


wizard_forms_fields = [
    {
        'template': 'popular_proposal/wizard/paso1.html',
        'explation_template': "popular_proposal/steps/paso1.html",
        'fields': OrderedDict([(
            'clasification', forms.ChoiceField(choices=TOPIC_CHOICES,
                                               widget=forms.Select())
        ),
            ('problem', forms.CharField(max_length=1024,
                                        widget=forms.Textarea()
                                        ))
        ])
    },
    {
        'template': 'popular_proposal/wizard/paso5.html',
        'explation_template': "popular_proposal/steps/paso5.html",
        'fields': OrderedDict([
            ('title', forms.CharField(max_length=256,
                                      widget=forms.TextInput())),
            ('is_local_meeting', forms.BooleanField(required=False)),
            ('generated_at', forms.ModelChoiceField(required=False,
                                                    queryset=get_possible_generating_areas(),
                                                    empty_label="No aplica")
                                                    ),
            ('terms_and_conditions', forms.BooleanField(
                error_messages={'required':
                                _(u'Debes aceptar nuestros Términos y Condiciones')}
            )
            ),
        ])
    }
]
