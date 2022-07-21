from django import forms
from django.contrib.auth.forms import UserCreationForm
from services.models.service import Service
from users.models.customer import Customer
from users.models.expert import Expert
from django.contrib.auth.forms import AuthenticationForm
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Div

from users.models.user import User


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=11, required=True)
    name = forms.CharField(required=True)

    class Meta:
        model = User
        fields = (
            "username",
            "name",
            "email",
            "phone_number",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)


class CustomerRegisterForm(UserRegisterForm):
    address = forms.CharField(
        label="",
        strip=False,
        widget=forms.Textarea(
            attrs={
                "placeholder": "محل سکونت",
                "style": "text-align: right; direction: rtl;",
            }
        ),
        help_text=None,
    )

    class Meta(UserRegisterForm.Meta):
        fields = UserRegisterForm.Meta.fields + ("address",)

    def save(self, commit=True):
        user = super(
            CustomerRegisterForm,
            self,
        ).save(commit=False)
        user.email = self.cleaned_data["email"]
        role = Customer.objects.create(address=self.cleaned_data["address"])
        user.role = role
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "نام کاربری"
        self.fields["name"].widget.attrs["placeholder"] = "نام و نام خانوادگی"
        self.fields["email"].widget.attrs["placeholder"] = "آدرس ایمیل"
        self.fields["phone_number"].widget.attrs["placeholder"] = "شماره تلفن همراه"
        self.fields["password1"].widget.attrs["placeholder"] = "رمز عبور"
        self.fields["password2"].widget.attrs["placeholder"] = "تکرار رمز عبور"
        self.fields["username"].label = ""
        self.fields["name"].label = ""
        self.fields["email"].label = ""
        self.fields["phone_number"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""
        self.fields["username"].help_text = None
        self.fields["name"].help_text = None
        self.fields["email"].help_text = None
        self.fields["phone_number"].help_text = None
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None
        self.fields["username"].widget.attrs[
            "style"
        ] = "text-align: right; direction: rtl;"
        self.fields["name"].widget.attrs["style"] = "text-align: right; direction: rtl;"
        self.fields["email"].widget.attrs[
            "style"
        ] = "text-align: right; direction: rtl;"
        self.fields["phone_number"].widget.attrs[
            "style"
        ] = "text-align: right; direction: rtl;"
        self.fields["password1"].widget.attrs[
            "style"
        ] = "text-align: right; direction: rtl;"
        self.fields["password2"].widget.attrs[
            "style"
        ] = "text-align: right; direction: rtl;"
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div(
                    Div("username", css_class="col"),
                    Div("name", css_class="col"),
                    css_class="row",
                ),
                Div(
                    Div("email", css_class="col"),
                    Div("phone_number", css_class="col"),
                    css_class="row",
                ),
                Div(
                    Div("password1", css_class="col"),
                    Div("password2", css_class="col"),
                    css_class="row",
                ),
                Div(Div("address", css_class="col"), css_class="row"),
                css_class="container complete-rtl px-0 mx-0",
            ),
            Submit(
                "submit",
                "ثبت نام",
                css_class="btn btn-dark py-2 mt-2",
                style="width: 10%",
            ),
        )


class ExpertRegisterForm(UserRegisterForm):
    document = forms.FileField()
    expertise = forms.ModelChoiceField(queryset=Service.objects.all(), required=True)

    class Meta(UserRegisterForm.Meta):
        fields = UserRegisterForm.Meta.fields + (
            "expertise",
            "document",
        )

    def save(self, commit=True):
        user = super(
            ExpertRegisterForm,
            self,
        ).save(commit=False)
        role = Expert.objects.create(
            expertise=self.cleaned_data["expertise"],
            document=self.cleaned_data["document"],
        )
        user.role = role
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "نام کاربری"
        self.fields["name"].widget.attrs["placeholder"] = "نام و نام خانوادگی"
        self.fields["email"].widget.attrs["placeholder"] = "آدرس ایمیل"
        self.fields["phone_number"].widget.attrs["placeholder"] = "شماره تلفن همراه"
        self.fields["password1"].widget.attrs["placeholder"] = "رمز عبور"
        self.fields["password2"].widget.attrs["placeholder"] = "تکرار رمز عبور"
        self.fields["expertise"].widget.attrs["placeholder"] = "انتخاب تخصص"
        self.fields["document"].widget.attrs["placeholder"] = "آپلود مدارک"
        self.fields["username"].label = ""
        self.fields["name"].label = ""
        self.fields["email"].label = ""
        self.fields["phone_number"].label = ""
        self.fields["password1"].label = ""
        self.fields["password2"].label = ""
        self.fields["expertise"].label = "انتخاب تخصص"
        self.fields["document"].label = "آپلود مدارک"
        self.fields["username"].help_text = None
        self.fields["name"].help_text = None
        self.fields["email"].help_text = None
        self.fields["phone_number"].help_text = None
        self.fields["password1"].help_text = None
        self.fields["password2"].help_text = None
        self.fields["expertise"].help_text = None
        self.fields["document"].help_text = None
        self.fields["username"].widget.attrs[
            "style"
        ] = "text-align: right; direction: rtl;"
        self.fields["name"].widget.attrs["style"] = "text-align: right; direction: rtl;"
        self.fields["email"].widget.attrs[
            "style"
        ] = "text-align: right; direction: rtl;"
        self.fields["phone_number"].widget.attrs[
            "style"
        ] = "text-align: right; direction: rtl;"
        self.fields["password1"].widget.attrs[
            "style"
        ] = "text-align: right; direction: rtl;"
        self.fields["password2"].widget.attrs[
            "style"
        ] = "text-align: right; direction: rtl;"
        self.fields["expertise"].widget.attrs[
            "style"
        ] = "text-align: left; direction: ltr;"
        self.fields["document"].widget.attrs[
            "style"
        ] = "text-align: left; direction: ltr;"
        self.helper = FormHelper(self)
        self.helper.layout = Layout(
            Div(
                Div(
                    Div("username", css_class="col"),
                    Div("name", css_class="col"),
                    css_class="row",
                ),
                Div(
                    Div("email", css_class="col"),
                    Div("phone_number", css_class="col"),
                    css_class="row",
                ),
                Div(
                    Div("password1", css_class="col"),
                    Div("password2", css_class="col"),
                    css_class="row",
                ),
                Div(
                    Div("expertise", css_class="col"),
                    css_class="row",
                ),
                Div(
                    Div("document", css_class="col"),
                    css_class="row",
                ),
                css_class="container complete-rtl px-0 mx-0",
            ),
            Submit(
                "submit",
                "ثبت نام",
                css_class="btn btn-dark py-2 mt-2",
                style="width: 10%",
            ),
        )


class LoginForm(AuthenticationForm):
    def __init__(self, request=None, *args, **kwargs) -> None:
        super().__init__(request, *args, **kwargs)
        self.fields["username"].widget.attrs["placeholder"] = "نام کاربری"
        self.fields["username"].label = ""
        self.fields["password"].label = ""
        self.fields["password"].widget.attrs["placeholder"] = "رمز عبور"
        self.fields["username"].widget.attrs[
            "style"
        ] = "text-align: right; direction: rtl;"
        self.fields["password"].widget.attrs[
            "style"
        ] = "text-align: right; direction: rtl;"
