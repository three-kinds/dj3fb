import factory
from django.contrib.auth.factories import UserFactory
from dj3fb.faker_utils import f
from .category_factory import CategoryFactory
from .licence_factory import LicenceFactory

from ..models import Movie


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    name = factory.Sequence(lambda _: f.pystr(max_chars=32))
    score = factory.Sequence(lambda _: f.pyfloat())
    ip_v4 = factory.Sequence(lambda _: f.ipv6())
    ip_v6 = factory.Sequence(lambda _: f.ipv4())
    info = factory.Sequence(lambda _: f.json())
    category = factory.SubFactory(CategoryFactory)
    licence = factory.SubFactory(LicenceFactory)
    inspector = factory.SubFactory(UserFactory)

    @factory.post_generation
    def actors(self, create, extracted, **_):
        if not create:
            return

        if extracted:
            for o in extracted:
                self.actors.add(o)
