import factory
from dj3fb.faker_utils import f
from .category_factory import CategoryFactory
from .licence_factory import LicenceFactory

from ..models import Movie


class MovieFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Movie

    name = factory.Sequence(lambda _: f.pystr(max_chars=32))
    category = factory.SubFactory(CategoryFactory)
    licence = factory.SubFactory(LicenceFactory)

    @factory.post_generation
    def actors(self, create, extracted, **_):
        if not create:
            return

        if extracted:
            for o in extracted:
                self.actors.add(o)
