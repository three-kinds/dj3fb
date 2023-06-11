import factory
from dj3fb.faker_utils import f

from ..models import Category


class CategoryFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Category

    name = factory.Sequence(lambda _: f.pystr(max_chars=32))
