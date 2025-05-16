from django.db import models
from django.contrib.auth.models import User

FORMAT_BO_CHOICES = [
    ('BO1', 'BO1'),
    ('BO3', 'BO3'),
    ('BO5', 'BO5'),
]

class Match(models.Model):
    equipe1 = models.CharField(max_length=100)
    equipe2 = models.CharField(max_length=100)
    date = models.DateTimeField()
    format_bo = models.CharField(max_length=4, choices=FORMAT_BO_CHOICES, default='BO3')

    def __str__(self):
        return f"{self.equipe1} vs {self.equipe2} ({self.format_bo})"

class Pari(models.Model):
    utilisateur = models.ForeignKey(User, on_delete=models.CASCADE)
    match = models.ForeignKey(Match, on_delete=models.CASCADE)
    choix = models.CharField(max_length=100)
    score_pari = models.CharField(max_length=10, blank=True, null=True)
    date_pari = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.utilisateur.username} : {self.choix} ({self.score_pari}) sur {self.match}"

