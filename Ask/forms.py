from django import forms
from .models import *


def get_topics():
    return  [(interest.id, interest.topic) for interest in Interest.objects.all()]

class QuestionForm(forms.ModelForm):

    question_text = forms.CharField(widget=forms.Textarea )
    class Meta:
        model = Question
        fields = ('question_text','topic_id')
    
    def __init__(self,*args,**kwargs):
        super(QuestionForm,self).__init__(*args,**kwargs)
        self.fields['question_text'].widget.attrs= { 
            'class':'form-control'
        }
        self.fields['topic_id'].widget.attrs={
            'class':'form-control'
        } 
        self.fields['topic_id'].choices = get_topics


class AnswerForm(forms.ModelForm):

    answer_text = forms.CharField(widget=forms.Textarea )
    class Meta:
        model = Answer
        fields = ('answer_text',)

    def __init__(self,*args,**kwargs):
        super(AnswerForm,self).__init__(*args,**kwargs)
        self.fields['answer_text'].widget.attrs= { 
            'class':'form-control'
        }
        