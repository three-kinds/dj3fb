import factory
from dj3fb.faker_utils import f

from ..models import Licence


class LicenceFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Licence

    content = factory.Sequence(lambda _: f.pystr(max_chars=32))
    category = factory.Iterator(['A', 'B', 'C'])
    price = factory.Sequence(lambda _: f.pydecimal(left_digits=3, right_digits=2))
    duration = factory.Sequence(lambda _: f.time_delta())
    file = factory.django.FileField()
    image = factory.django.ImageField()
    file_path = factory.Sequence(lambda _: f.file_path())
    file_binary = factory.Sequence(lambda _: memoryview(f.binary(1024)))
    url = factory.Sequence(lambda _: f.url())
    uuid = factory.Sequence(lambda _: f.uuid4())
    created_time = factory.Sequence(lambda _: f.time())
    created_date = factory.Sequence(lambda _: f.date_this_century())
    created_datetime = factory.Sequence(lambda _: f.date_time_this_century())
