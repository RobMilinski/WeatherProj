from django.test import TestCase
from .views import weatherapp
import unittest

# Create your tests here.

class BasicTests(unittest.TestCase):
    response = weatherapp()
    self.assertEqual(response.status_code, 200)