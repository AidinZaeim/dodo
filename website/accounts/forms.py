from django import forms
from .models import CustomUser


class RegisterForm(forms.ModelForm):
    Email = forms.EmailField(max_length=255)
    Password1 = forms.CharField(widget=forms.PasswordInput)
    Password2 = forms.CharField(widget=forms.PasswordInput)

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["Password2"] and cd["Password1"] and cd['password1'] != cd['password2']:
            raise forms.ValidationError("رمز ها یکسان نیست")

    class Meta:
        model = CustomUser
        fields = ["Email", "Password1", "Password2"]
