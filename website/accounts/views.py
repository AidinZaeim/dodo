from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import CustomUser
from django.forms import ValidationError
from django.views import View
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.views import LoginView

message_dict = {
    "short": "رمز عبور باید حداقل ۸ کاراکتر باشد",
    "common": "رمز عبور تکراری است؛",
    "all_numeric": "رمز عبور باید شامل حروف نیز باشد",
    "signed_up": "ثبت نام با موفقیت انجام شد"
}


class CustomUserRegister(View):

    def get(self, request):
        return render(request, "accounts/register.html", {"forms": RegisterForm(request.POST)})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            try:
                validate_password(cd["Password1"])
            except ValidationError as validation_error:
                for message in validation_error:
                    if ('This password is too short. It must contain at least 8 characters.' == message):
                        messages.error(request,message_dict["short"] )
                    if ('This password is too common.' == message):
                        messages.error(request, message_dict["common"])
                    if ('This password is entirely numeric.' == message):
                        messages.error(request,message_dict["all_numeric"])
                return redirect("accounts:register")

            CustomUser.objects.create_user(cd["Email"], cd["Password1"])
            messages.success(request, message_dict["signed_up"])
            return redirect("accounts:login")

        return render(request, "accounts:register", {"form": self.form})


class CustomLoginView(LoginView):
    template_name = 'accounts/login.html'

    def form_valid(self, form):
        return super().form_valid(form)

    def get_success_url(self):
        return redirect("panel:management")