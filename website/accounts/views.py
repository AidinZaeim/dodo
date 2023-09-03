from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import RegisterForm, LoginForm
from .models import CustomUser
from django.forms import ValidationError
from django.views import View
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.password_validation import validate_password


message_dict = {
    "short": "رمز عبور باید حداقل ۸ کاراکتر باشد",
    "common": "رمز عبور تکراری است؛",
    "all_numeric": "رمز عبور باید شامل حروف نیز باشد",
    "signed_up": "ثبت نام با موفقیت انجام شد",
    "integrity_error": "ایمیل تکراری است",
    "login": "ورود با موفقیت انجام شد",
    "login_error": "خظا در ورود: کاربر وجود ندارد"
}


class CustomUserRegister(View):

    def get(self, request):
        return render(request, "accounts/register.html", {"forms": RegisterForm(request.POST)})

    def post(self, request):
        form = RegisterForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            print(cd)
            existing_users = CustomUser.objects.filter(email=cd["Email"]).exists()
            if existing_users:
                messages.error(request,message_dict["integrity_error"])
                return redirect(request.META.get('HTTP_REFERER'))
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

        return render(request, "accounts/register.html", {"form": self.form})


class CustomLoginView(View):
    def get(self, request):
        return render(request, "accounts/login.html", {"form": LoginForm})

    def post(self, request):
        form = LoginForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            user = authenticate(request, email=cd['UserName'], password=cd['Password'])
            if user is not None:
                login(request, user)
                messages.success(request, message_dict["login"])
                if 'next' in request.GET:
                    return redirect(request.GET['next'])
                else:
                    return redirect("panel:management")
            else:
                messages.error(request, message_dict['login_error'])
                return redirect("accounts:login")
