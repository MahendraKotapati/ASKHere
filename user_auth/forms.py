from django import forms 
from Ask.models import UserLogin

class SignUpForm(forms.ModelForm):
    '''username = forms.CharField(max_length=100,required=True)
    email = forms.EmailField(required=True)
    password = forms.CharField(widget=forms.PasswordInput())'''

    class Meta:
        model = UserLogin
        fields = ('username','password','email')

    def __init__(self,*args,**kwargs):

        super(SignUpForm,self).__init__(*args,**kwargs)

        self.fields['username'].widget.attrs ={
            'class':'form-control'
        }
        self.fields['email'].widget.attrs ={
            'class':'form-control'
        }
        self.fields['password'].widget.attrs ={
            'class':'form-control'
        }
    
    

