from django import forms
from django.contrib.auth.forms import UserCreationForm
from users.models.customer import Customer
from users.models.expert import Expert


class CustomerRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=10, required=True)

    class Meta:
        model = Customer
        fields = ("username", "email", "phone_number", "password1", "password2")

    def save(self, commit=True):
        user = super(
            CustomerRegisterForm,
            self,
        ).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user


class ExpertRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=10, required=True)

    class Meta:
        model = Expert
        fields = ("username", "email", "phone_number", "password1", "password2")

    def save(self, commit=True):
        user = super(
            ExpertRegisterForm,
            self,
        ).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user
