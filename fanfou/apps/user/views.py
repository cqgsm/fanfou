from django.contrib.auth import login, logout ,authenticate
from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseRedirect
from django.views.generic.base import View, TemplateResponseMixin, RedirectView

from fanfou.apps.user.forms import LoginForm


# from django.views.decorators.csrf import csrf_exempt
# from django.utils.decorators import method_decorator

class LoginView(View, TemplateResponseMixin):
    redirect_url = None
    def get(self, request, *args, **kwargs):
        form = LoginForm()
        return render(request, self.get_template_names(),{'form':form})
        
    def post(self, request, *args, **kwargs):
        form = LoginForm(request.POST)
        if form.is_valid():
            user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect(self.redirect_url)
        return self.get(request)
    
    
class LogoutView(RedirectView):
    permanent = False
    def get(self, request, *args, **kwargs):
        logout(request)
        return super(LogoutView, self).get(self, request, *args, **kwargs)


# @csrf_exempt
# def api_login(request, redirect_url):
#     from rest_framework.authtoken.models import Token
#     if request.method == "POST":
#         form = LoginForm(request.POST)
#         if form.is_valid():
#             user = authenticate(username = form.cleaned_data['username'], password = form.cleaned_data['password'])
#             if user is not None:
#                 if user.is_active:
#                     login(request, user)
#                     token, _ = Token.objects.get_or_create(user=user)
#                     request.session['Authorization'] = token.key
#                     return HttpResponseRedirect(redirect_url)
#         return render(request, "rest_framework/login.html")
#     else:
#         return render(request, "rest_framework/login.html")
#
# def api_logout(request, redirect_url):
#     logout(request)
#     return redirect(redirect_url)
