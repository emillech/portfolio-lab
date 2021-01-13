from clothes_giver.models import Category, Institution, Donation
from faker import Faker
import random
import lorem
import datetime


fake = Faker()


def add_category():
    Category.objects.create(name='Clothes')
    Category.objects.create(name='Food')
    Category.objects.create(name='Kitchen stuff')
    Category.objects.create(name='Electrical devices')
    Category.objects.create(name='Bedding')


def add_institution():

    for _ in range(15):
        all_categories = Category.objects.all()
        category = random.choice(all_categories)
        company_name = fake.company()
        i = Institution.objects.create(
            name=company_name,
            description=lorem.paragraph(),
            type=random.randint(1, 3),
        )

        i.categories.add(category)


def add_donation():
    for _ in range(30):
        all_categories = Category.objects.all()
        category = random.choice(all_categories)
        all_institution = Institution.objects.all()
        institution = random.choice(all_institution)
        today = datetime.date.today()
        date = fake.date_between(start_date=today)
        d = Donation.objects.create(
            quantity=random.randint(1, 10),
            institution=institution,
            address=fake.address(),
            phone_number=random.randint(100000000, 999999999),
            city=fake.city(),
            zip_code=str(random.randint(00000, 99999)),
            pick_up_date=date,
            pick_up_time=fake.date_time_between(start_date=date, end_date=date),
            pick_up_comment=lorem.paragraph(),
        )
        d.categories.add(category)





# add_category()
# add_institution()
add_donation()