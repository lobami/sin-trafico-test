from rest_framework.test import APITestCase
from users.models import User
from center.factories import UserFactory, UnitFactory


class UserViewSetTestCase(APITestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username='admin@testcase.com',
            email='admin@testcase.com',
            password='testcase',
            role='superadmin')
        result = self.client.post('/api/token/', {
            'username': 'admin@testcase.com',
            'password': 'testcase'
        })
        self.user_test = UserFactory.create()
        self.unit_test = UnitFactory.create(user=self.user_test)
        self.unit_test_no = UnitFactory.create()
        self.token = result.data['token']

    def test_get_user(self):
        result = self.client.get('/api/1/users/{}/'.format(str(self.user_test.id)),
                                  HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(result.status_code, 200)

    def test_get_units(self):
        units = self.client.get('/api/1/units/?user={}/'.format(str(self.user_test.id)),
                                 HTTP_AUTHORIZATION='Bearer ' + self.token)
        result_good = self.client.get('/api/1/users/{}/units/'.format(str(self.user_test.id)),
                                 HTTP_AUTHORIZATION='Bearer ' + self.token)
        self.assertEqual(result_good.data[0]['id'], units.data['results'][0]['id'])


