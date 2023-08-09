from django.test import TestCase
from restaurant.models import Menu



class MenuViewTest(TestCase):
    def setUp(self):
        # Setup method to add test instances of the Menu model
        self.menu1 = Menu.objects.create(Title="IceCream", Price=80, Inventory=100)
        self.menu2 = Menu.objects.create(Title="Paleta", Price=30, Inventory=100)

    def test_getall(self):
        # Test to retrieve all the Menu objects and check serialized data
        menu = Menu.objects.all()

        # Serialize the retrieved data and check if it matches the expected data
        expected_data = '[<Menu: IceCream : 80.0>, <Menu: Paleta : 30.0>]'
        self.assertEqual(str(list(menu)),expected_data)