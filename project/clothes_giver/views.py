from django.shortcuts import render, redirect
from django.views import View
from clothes_giver.models import Category, Institution, Donation


class LandingPage(View):

    def get(self, request):

        return render(request, 'index.html')


class AddDonation(View):

    def get(self, request):

        return render(request, 'form.html')


class Login(View):

    def get(self, request):
        return render(request, 'login.html')


class Register(View):

    def get(self, request):
        return render(request, 'register.html')