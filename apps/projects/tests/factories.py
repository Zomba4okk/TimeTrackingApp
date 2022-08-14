import factory
from factory import fuzzy

from apps.projects.models import Project


class ProjectFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Project

    name = factory.Sequence(lambda n: f"Project-{n}")
    description = fuzzy.FuzzyText(length=100)
