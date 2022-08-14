import factory

from apps.users.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Sequence(lambda n: f"email.{n}@gmail.com")
    first_name = factory.Faker("first_name")
    last_name = factory.Faker("last_name")
