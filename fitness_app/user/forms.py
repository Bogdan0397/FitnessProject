from django import forms
from django.contrib.auth import get_user_model
from django.contrib.auth.forms import AuthenticationForm, UserCreationForm


class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Login', widget=forms.TextInput(attrs={'class':'form-input'}))
    password = forms.CharField(label='Password', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['username','password']


class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Login',widget=forms.TextInput(attrs={'class':'form-input'}))
    email = forms.EmailField(label='Email',widget=forms.TextInput(attrs={'class':'form-input'}))
    first_name = forms.CharField(label='Name', widget=forms.TextInput(attrs={'class':'form-input'}))
    last_name = forms.CharField(label='Surname', widget=forms.TextInput(attrs={'class': 'form-input'}))


    class Meta:
        model = get_user_model()
        fields = ['username', 'email', 'first_name', 'last_name','password1', 'password2']
        labels = {'email': 'Email',
                  'first_name': 'Name',
                  'last_name':'Surname',
                  }

        widgets = {'email': forms.TextInput(attrs={'class':'form-input'}),
                  'first_name': forms.TextInput(attrs={'class':'form-input'}),
                  'last_name':forms.TextInput(attrs={'class':'form-input'})
                   }



    def clean_email(self):
        email = self.cleaned_data['email']
        if get_user_model().objects.filter(email=email).exists():
            raise forms.ValidationError("Email already exist")
        return email

class ProfileUserForm(forms.ModelForm):
    username = forms.CharField(disabled=True,required=False, label='Username', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.CharField(disabled=True,required=False, label='Email', widget=forms.TextInput(attrs={'class': 'form-input'}))

    class Meta:
        model = get_user_model()
        fields = ['photo','username','email','first_name','last_name','weight','height','gender']

        labels = {'email': 'Email',
                  'first_name': 'Name',
                  'last_name':'Surname',
                  'weight': 'Weight',
                  'height': 'Height',
                  'gender':'Gender',
                  'photo': 'Photo',
                  }

        widgets = {'email': forms.TextInput(attrs={'class':'form-input'}),
                  'first_name': forms.TextInput(attrs={'class':'form-input'}),
                  'last_name':forms.TextInput(attrs={'class':'form-input'}),
                  'photo': forms.FileInput}

