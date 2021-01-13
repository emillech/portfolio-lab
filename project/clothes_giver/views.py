from django.shortcuts import render, redirect
from django.views import View
from clothes_giver.models import Category, Institution, Donation


class LandingPage(View):

    def get(self, request):
        quantity = 0
        all_donations = Donation.objects.all()
        for donation in all_donations:
            quantity += donation.quantity

        number_of_institutions = Institution.objects.count()

        foundations = Institution.objects.filter(type=1)
        foundations_data = {}
        for foundation in foundations:
            categories = Category.objects.filter(institution=foundation)
            foundations_data.update({foundation: categories})

        ngos = Institution.objects.filter(type=2)
        ngos_data = {}
        for ngo in ngos:
            categories = Category.objects.filter(institution=ngo)
            ngos_data.update({ngo: categories})

        locals = Institution.objects.filter(type=3)
        locals_data = {}
        for local in locals:
            categories = Category.objects.filter(institution=local)
            locals_data.update({local: categories})

        ctx = {
            'quantity': quantity,
            'institutions': number_of_institutions,
            'foundations': foundations_data,
            'ngo': ngos_data,
            'local': locals_data
        }
        return render(request, 'index.html', ctx)


class AddDonation(View):

    def get(self, request):

        return render(request, 'form.html')


class Login(View):

    def get(self, request):
        return render(request, 'login.html')


class Register(View):

    def get(self, request):
        return render(request, 'register.html')