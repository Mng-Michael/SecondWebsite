from django import forms
from . import models
from django.forms import ModelForm
from django import forms


class ScoreForm(ModelForm):
    class Meta:
        model = models.Score
        fields = ('leaderboard', 'score', 'source', 'clean_code')
