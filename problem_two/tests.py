import unittest

from pymongo import MongoClient

from main import create_customer
from main import create_order
from main import retrieve_customers

client = MongoClient()

# Connect with the portnumber and host
client = MongoClient('mongodb://localhost:27017/')

# Access datab
mydatabase = client['DominosDB']


class DB_Tests(unittest.TestCase):
    # Dummy
    def test_customer_name_type_check(self):
        with self.assertRaises(TypeError):
            create_customer(234, 234, 23)
    # Dummy

    def test_customer_num_goods_type_check(self):
        with self.assertRaises(TypeError):
            create_customer('Sriram', '234', 23)
    # Dummy

    def test_customer_id_type_check(self):
        with self.assertRaises(TypeError):
            create_customer('Sriram', '234', 23)
    # mock

    def test_add_customer(self):
        create_customer('Sriram', 234, 23)
        customer = mydatabase.customer_info.find_one({'id': 23})
        self.assertEqual(customer['name'], 'Sriram')
        self.assertEqual(customer['num_goods'], 234)
        self.assertEqual(customer['id'], 23)
        mydatabase.customer_info.delete_one({'id': 23})
    # Dummy

    def test_create_order_invalid_id_check(self):
        with self.assertRaises(ValueError):
            create_order(567)
    # Mock

    def test_create_order(self):
        create_customer('Sriram', 234, 23)
        create_order(23)
        customer = mydatabase.customer_info.find_one({'id': 23})
        order = mydatabase.orders.find_one({'customer_id': 23})
        self.assertEqual(customer['num_goods'], 235)
        self.assertEqual(order['num_goods'], 235)
        mydatabase.orders.delete_one({'customer_id': 23})
        mydatabase.customer_info.delete_one({'id': 23})
    # Stub

    def test_create_duplicate_id(self):
        create_customer('Rishabh', 234, 34)
        with self.assertRaises(ValueError):
            create_customer('Sriram', 234, 34)
        query = {'id': 34}
        mydatabase.customer_info.delete_one(query)
    # mock

    def test_retrieve_customers(self):
        result = retrieve_customers()

        customers = []

        for customer in mydatabase.customer_info.find():
            customers.append(customer)

        self.assertEqual(customers, result)
