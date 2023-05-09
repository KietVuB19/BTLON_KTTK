from django import forms
from django.core.exceptions import ValidationError
from users.models import User

class LoginForm(forms.Form):
    email = forms.CharField(max_length=255, required=True)
    password = forms.CharField(max_length=255, required=True)

    def clean(self):
        cleaned_data = super().clean()
        email = cleaned_data['email']
        password = cleaned_data['password']
        try:
            user = User.objects.get(email=email)
            if user.password != password:
                raise ValidationError('Password is incorrect')
        except User.DoesNotExist:
            raise ValidationError('User does not exist')
        return cleaned_data

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(max_length=255, required=True)

    class Meta:
        model = User
        fields = ('email', 'password', 'full_name', 'address')

    def clean_confirm_password(self):
        password = self.cleaned_data.get('password')
        confirm_password = self.cleaned_data.get('confirm_password')
        if password and confirm_password:
            if password != confirm_password:
                raise forms.ValidationError('Passwords do not match')
        return confirm_password
