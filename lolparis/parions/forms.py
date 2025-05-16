from django import forms
from .models import Pari

class PariForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        match = kwargs.pop('match', None)
        super().__init__(*args, **kwargs)

        if match:
            self.fields['choix'] = forms.ChoiceField(
                choices=[
                    (match.equipe1, match.equipe1),
                    (match.equipe2, match.equipe2),
                ],
                widget=forms.RadioSelect,
                label="Choisissez l'équipe gagnante"
            )

        self.fields['score_pari'] = forms.ChoiceField(
            choices=[
                ("2-0", "2-0"),
                ("2-1", "2-1"),
                ("3-0", "3-0"),
                ("3-1", "3-1"),
                ("3-2", "3-2"),
            ],
            widget=forms.Select,
            label="Score exact (BO3 ou BO5)",
            required=True
        )

    class Meta:
        model = Pari
        fields = ['choix', 'score_pari']
