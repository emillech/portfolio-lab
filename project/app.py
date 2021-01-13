from clothes_giver.models import Category, Institution, Donation
from faker import Faker
import random
import lorem


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


# add_category()
# add_institution()