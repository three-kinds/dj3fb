import factory
from dj3fb.faker_utils import f

from django.contrib.auth.models import User


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    password = factory.Sequence(lambda _: f.pystr(max_chars=128))
    last_login = factory.Sequence(lambda _: f.date_time_this_century())
    is_superuser = factory.Sequence(lambda _: f.boolean())
    username = factory.Sequence(lambda _: f.pystr(max_chars=150))
    first_name = factory.Sequence(lambda _: f.pystr(max_chars=150))
    last_name = factory.Sequence(lambda _: f.pystr(max_chars=150))
    email = factory.Sequence(lambda _: f.email())
    is_staff = factory.Sequence(lambda _: f.boolean())
    is_active = factory.Sequence(lambda _: f.boolean())
    date_joined = factory.Sequence(lambda _: f.date_time_this_century())

    @factory.post_generation
    def groups(self, create, extracted, **_):
        if not create:
            return

        if extracted:
            for o in extracted:
                self.groups.add(o)

    @factory.post_generation
    def user_permissions(self, create, extracted, **_):
        if not create:
            return

        if extracted:
            for o in extracted:
                self.user_permissions.add(o)
