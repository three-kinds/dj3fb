import factory
from dj3fb.faker_utils import f

from ..models import Licence


class LicenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Licence

    content = factory.Sequence(lambda _: f.pystr(max_chars=32))
