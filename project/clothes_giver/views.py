from django.shortcuts import render, redirect
from django.views import View
from clothes_giver.models import Category, Institution, Donation
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login
from django.contrib.auth.mixins import LoginRequiredMixin


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

        user = request.user

        ctx = {
            'quantity': quantity,
            'institutions': number_of_institutions,
            'foundations': foundations_data,
            'ngo': ngos_data,
            'local': locals_data,
            'user': user,
        }
        return render(request, 'index.html', ctx)


class AddDonation(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        all_categories = Category.objects.all()
        all_institution = Institution.objects.all()
        institutions_dict = {}

        for institution in all_institution:
            categories = Category.objects.filter(institution=institution)
            institutions_dict.update({institution: categories})

        ctx = {
            'categories': all_categories,
            'institutions': all_institution,
            'dict': institutions_dict,
        }

        return render(request, 'form.html', ctx)

    def post(self, request):

        user = request.user
        quantity = request.POST.get('bags')
        categories = request.POST.get('categories')

        institution = request.POST.get('institution_name')
        institution_object = Institution.objects.get(name=institution)
        address = request.POST.get('address')
        phone_number = int(request.POST.get('phone'))
        city = request.POST.get('city')
        zip_code = request.POST.get('postcode')
        pick_up_date = request.POST.get('data')
        pick_up_time = request.POST.get('time')
        pick_up_comment = request.POST.get('more_info')

        try:
            Donation.objects.create(
                quantity=quantity,
                institution=44,
                address=address,
                phone_number=phone_number,
                city=city,
                zip_code=zip_code,
                pick_up_date=pick_up_date,
                pick_up_time=pick_up_time,
                pick_up_comment=pick_up_comment,
                user=user
            )
            return redirect('/')

        except:
            return redirect('/login/')


class Login(View):

    def get(self, request):
        return render(request, 'login.html')

    def post(self, request):
        username = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            return redirect('/register/')


class Register(View):

    def get(self, request):
        return render(request, 'register.html')

    def post(self, request):
        name = request.POST.get('name')
        surname = request.POST.get('surname')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password_2 = request.POST.get('password2')

        if password == password_2:
            User.objects.create_user(
                username=email,
                password=password,
                email=email,
                first_name=name,
                last_name=surname)

        return redirect('/login/')


class LogoutView(View):
    """
    A class used to represent a Logout. It does not need template.
    """

    def get(self, request):
        """
        This method logout user and redirect him to index.
        """
        logout(request)
        return redirect("/")


class UserView(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):

        user = request.user
        user_donations = Donation.objects.filter(user=user).order_by('is_taken')

        donation_dict = {}

        for donation in user_donations:
            categories = Category.objects.filter(institution=donation.institution)
            donation_dict.update({donation: categories})

        ctx = {
            'user': user,
            'donations': donation_dict
        }

        return render(request, 'user_site.html', ctx)

    def post(self, request):

        donation_id = request.POST.get('donation_id')
        int(donation_id)
        chosen_donation = Donation.objects.get(id=donation_id)
        chosen_donation.is_taken = True
        chosen_donation.save()

        user = request.user
        user_donations = Donation.objects.filter(user=user).order_by('is_taken')

        donation_dict = {}

        for donation in user_donations:
            categories = Category.objects.filter(institution=donation.institution)
            donation_dict.update({donation: categories})

        ctx = {
            'user': user,
            'donations': donation_dict,
            'aaa': chosen_donation
        }

        return render(request, 'user_site.html', ctx)


class EditUser(LoginRequiredMixin, View):
    login_url = '/login/'

    def get(self, request):
        return render(request, 'edit_user.html')

    def post(self, request):

        user = request.user
        # password = user.password
        old_password = request.POST.get('old_password')
        new_password = request.POST.get('new_password')
        new_password_2 = request.POST.get('new_password2')
        text = ''

        user = authenticate(username=user.username, password=old_password)
        if user is not None:
            if new_password == new_password_2:
                user.set_password(new_password)
                user.save()
                text = 'Hasło zostało zmienione'
            else:
                text = 'Hasła nie pasują do siebie'
        else:
            text = 'Podałeś błędne hasło'

        ctx = {
            'text': text,
        }

        return render(request, 'edit_user.html', ctx)


class ConfirmationView(View):

    def get(self, request):
        return render(request, 'form-confirmation.html')