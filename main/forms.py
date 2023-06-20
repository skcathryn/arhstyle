from django import forms
from django.core.exceptions import ValidationError
from django.forms import Textarea
from main.models import *


class UserCreationForm(forms.ModelForm):
# Форма для создания пользователя

    password1 = forms.CharField(label="Пароль", widget=forms.PasswordInput, min_length=6)
    password2 = forms.CharField(label="Повторите пароль", widget=forms.PasswordInput, min_length=6)

    rules = forms.BooleanField(label="Согласен с условиями регистриции", required=True)

    class Meta:
        model = User
        fields = ["username", "name", "surename", "patronymic", "email", "password1", "password2", "rules"]

    def clean_password2(self):
        # Проверка паролей на совпадение
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user

