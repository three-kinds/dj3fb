import factory
from dj3fb.faker_utils import f

from ..models import Cinema


class CinemaFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Cinema

    int_array = factory.Sequence(lambda _: [f.pyint(10000, 99999) for _ in range(5)])
    int_choice_array = factory.Sequence(lambda _: [f.random_element([0, 1, 2, 3, 4, 5, 6, 7, 8, 9]) for _ in range(5)])
    char_choice_array = factory.Sequence(lambda _: [f.random_element(['A', 'B']) for _ in range(3)])
