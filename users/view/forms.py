from django import forms
from users.controller.controller import UserController
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


class UserUpdateForm(forms.ModelForm):
    email = forms.EmailField(required=True)
    phone_number = forms.CharField(max_length=11, required=True)
    name = forms.CharField(required=True)
    password1 = forms.CharField(required=False, widget=forms.PasswordInput)
    password2 = forms.CharField(required=False, widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = (
            "username",
            "name",
            "email",
            "phone_number",
            "password1",
            "password2",)

    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

class CustomerEditProfileForm(UserUpdateForm):

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

    def clean(self):
        if (self.cleaned_data["password1"] != self.cleaned_data["password2"]):
            raise forms.ValidationError("دو رمز عبور واردشده یکسان نمی باشند.")
        if (UserController.check_username_is_repetitive(self.customer.pk, self.cleaned_data["username"])):
            raise forms.ValidationError("نام کاربری وارد شده تکرای می باشد.")
        if (UserController.check_email_is_repetitive(self.customer.pk, self.cleaned_data["email"])):
            raise forms.ValidationError("ایمیل وارد شده تکرای می باشد.")
        
    class Meta(UserUpdateForm.Meta):
        fields = UserUpdateForm.Meta.fields + ("address",)

    def save(self, customer):
        customer.username = self.cleaned_data["username"]
        customer.name = self.cleaned_data["name"]
        customer.email = self.cleaned_data["email"]
        customer.phone_number = self.cleaned_data["phone_number"]
        customer.role.address = self.cleaned_data["address"]
        customer.role.save()
        customer.save()

    def __init__(self, customer, *args, **kwargs) -> None:
        self.customer = customer
        super().__init__(*args, **kwargs)
        
        self.fields["username"].initial = customer.username
        self.fields["name"].initial = customer.name
        self.fields["email"].initial = customer.email
        self.fields["phone_number"].initial = customer.phone_number
        self.fields["password1"].widget.attrs["placeholder"] = "رمز عبور جدید"
        self.fields["password2"].widget.attrs["placeholder"] = "تکرار رمز عبور جدید"
        self.fields["address"].initial = customer.role.address

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
                "Save",
                "ذخیره",
                css_class="btn btn-dark py-2 mt-2",
                style="width: 10%",
            ),
        )


class ExpertEditProfileForm(UserRegisterForm):
    document = forms.FileField()
    expertise = forms.ModelChoiceField(queryset=Service.objects.all(), required=True)

    def clean(self):
        pass
        #TODO

    class Meta(UserRegisterForm.Meta):
        fields = UserRegisterForm.Meta.fields + (
            "expertise",
            "document",
        )

    def save(self, expert):
        expert.username = self.cleaned_data["username"]
        expert.name = self.cleaned_data["name"]
        expert.email = self.cleaned_data["email"]
        expert.phone_number = self.cleaned_data["phone_number"]
        expert.role.expertise = self.cleaned_data["expertise"]
        expert.role.document = self.cleaned_data["document"]
        expert.role.save()
        expert.save()

    def __init__(self, expert, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.fields["username"].initial = expert.username
        self.fields["name"].initial = expert.name
        self.fields["email"].initial = expert.email
        self.fields["phone_number"].initial = expert.phone_number
        self.fields["password1"].widget.attrs["placeholder"] = "رمز عبور جدید"
        self.fields["password2"].widget.attrs["placeholder"] = "تکرار رمز عبور جدید"
        self.fields["expertise"].initial = expert.role.expertise
        self.fields["document"].initial = expert.role.document

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
                "ُSave",
                "ذخیره",
                css_class="btn btn-dark py-2 mt-2",
                style="width: 10%",
            ),
        )
