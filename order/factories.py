import factory

from django.contrib.auth.models import User
from product.factories import ProductFactory

from .models import Order


class UserFactory(factory.django.DjangoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')
    
    class Meta:
        model = User

class OrderFactory(factory.django.DjangoModelFactory):
    user = factory.SubFactory(userFactory)
    
    @factory.post_generation
    def product(self, create, extracted, **kwargs):
        if not create:
            return
        
        if extracted:
            for product in extracted:
                self.product.add(product)
    
    class Meta:
        model = Order