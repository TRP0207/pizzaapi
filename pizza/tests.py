from django.test import TestCase
from django.contrib.auth.models import User
from .models import Pizza

class PizzaTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        testuser1 = User.objects.create_user(
            username='testsuser1',password='abc123'
        )
        testuser1.save()

        test_pizza = Pizza.objects.crerate(
            author=testuser1, name='Pizza name',toppings='toppings'
        )
        test_pizza.save()

    def test_pizza_detail(self):
        pizza = Pizza.objects.get(id=1)
        expected_name = f'{pizza.name}'
        expected_toppings = f'{pizza.toppings}'
        self.assertEqual(expected_name, 'Blog name')
        self.assertEqual(expected_toppings, 'toppings')

