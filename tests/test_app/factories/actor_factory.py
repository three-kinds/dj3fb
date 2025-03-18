import factory
from dj3fb.faker_utils import f

from ..models import Actor


class ActorFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Actor

    name = factory.Sequence(lambda _: f.pystr(max_chars=32))
    age = factory.Sequence(lambda _: f.pyint(10000, 99999))
