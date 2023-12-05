from django import forms
from django.core import validators
from django.core.exceptions import ValidationError
from .models import User


class RegisterForm(forms.ModelForm):
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'کلمه عبور'}),
        validators=[validators.MaxLengthValidator(100)]
    )
    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control py-4', 'placeholder': 'تکرار کلمه عبور'}),
        validators=[validators.MaxLengthValidator(100)]
    )

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', 'mobile', 'national_code', 'address']
        widgets = {
            'email': forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'ایمیل'}),
            'first_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'نام خانوادگی'}),
            'mobile': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'شماره تلفن'}),
            'national_code': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'کد ملی'}),
            'address': forms.Textarea(attrs={'class': 'form-control', 'placeholder': 'آدرس'}),
        }

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        confirm_password = cleaned_data.get('confirm_password')

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError('کلمه عبور و تکرار آن مطابقت ندارند.')

        mobile = cleaned_data.get('mobile')
        if len(mobile) != 11 or not mobile.startswith('09'):
            raise forms.ValidationError('شماره تلفن باید ۱۱ رقمی و با 09 شروع شود.')

        return cleaned_data


class LoginForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(attrs={'class': 'form-control'}),
        validators=[
            validators.MaxLengthValidator(100)
        ]
    )


class ForgotPasswordForm(forms.Form):
    email = forms.EmailField(
        label='ایمیل',
        widget=forms.EmailInput(),
        validators=[
            validators.MaxLengthValidator(100),
            validators.EmailValidator
        ]
    )


class ResetPasswordForm(forms.Form):
    password = forms.CharField(
        label='کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )

    confirm_password = forms.CharField(
        label='تکرار کلمه عبور',
        widget=forms.PasswordInput(),
        validators=[
            validators.MaxLengthValidator(100),
        ]
    )
