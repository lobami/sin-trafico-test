import factory
from faker import Factory
from users.models import User
from units.models import Unit
from trackings.models import Tracking


faker = Factory.create()


class UserFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = User

    email = factory.Faker("safe_email")
    username = factory.LazyAttribute(lambda x: faker.name())
    first_name = factory.LazyAttribute(lambda x: faker.name())
    last_name = factory.LazyAttribute(lambda x: faker.name())
    password = factory.LazyAttribute(lambda x: faker.password())
    is_active = True
    @classmethod
    def _prepare(cls, create, **kwargs):
        password = kwargs.pop("password", None)
        user = super(UserFactory, cls)._prepare(create, **kwargs)
        if password:
            user.set_password(password)
            if create:
                user.save()
        return user


class UnitFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Unit
    name = factory.LazyAttribute(lambda x: faker.name())
    user = factory.SubFactory('center.factories.UserFactory')
    plates = factory.LazyAttribute(lambda x: faker.name())


class TrackingFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Tracking
    name = factory.LazyAttribute(lambda x: faker.name())
    unit = factory.SubFactory('center.factories.UnitFactory')
    lat = 20.1324523
    long = -100.78945

