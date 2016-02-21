# -*- coding: utf-8 -*-
from django.forms import ModelForm	
from cms.models import Record, Review

class RecordForm(ModelForm):
    '''書籍のフォーム'''
    class Meta:
        model = Record
        fields = ('album', 'artist', 'year', )

class ReviewForm(ModelForm):
    '''感想のフォーム'''
    class Meta:
        model = Review
        fields = ('comment', )
