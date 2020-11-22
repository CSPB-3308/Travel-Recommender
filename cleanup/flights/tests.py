from django.test import TestCase
from .models import testFlightData
from django.urls import reverse, resolve
from flights.views import flight_detail_view, create_flight_view, login, index, register, picker, flights, python_example

### great link for how to test URLS
###https://www.youtube.com/watch?v=0MrgsYswT1c&list=PLbpAWbHbi5rMF2j5n6imm0enrSD9eQUaM&index=2
class SampleFlightsTestCase(TestCase):
    @classmethod
    def setUpTestData(cls):
        pass
#the URL tests are Unittests to ensure the proper URLs render and that the views and url file are interacting properly
    def testDetail_URL(self):
        url = reverse('detail')
        print(resolve(url))
        self.assertEquals(resolve(url).func, flight_detail_view)

    def testCreate_URL(self):
        url = reverse('create_flight')
        print(resolve(url))
        self.assertEquals(resolve(url).func, create_flight_view)

    def testIndex_URL(self):
        url = reverse('index')
        self.assertEquals(resolve(url).func, index)

    def testLogin_URL(self):
        url = reverse('login')
        self.assertEquals(resolve(url).func, login)

    def testRegister_URL(self):
        url = reverse('register')
        self.assertEquals(resolve(url).func, register)

    def testFlights_URL(self):
        url = reverse('flights')
        self.assertEquals(resolve(url).func, flights)

    def testPicker_URL(self):
        url = reverse('picker')
        self.assertEquals(resolve(url).func, picker)

    def testPicker_URL(self):
        url = reverse('python_example')
        self.assertEquals(resolve(url).func, python_example)


    def test3(self):
        pass