import uuid, dateutil
from decimal import Decimal

from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse

from core.models import People, Company, Food, Tag
from core.serializers import EmployeesSerializer

def pre_load_companies():
    company_data = [
        {
            "index": 1,
            "company": "NETBOOK"
        },
        {
            "index": 2,
            "company": "PERMADYNE"
        },
        {
            "index": 3,
            "company": "LINGOAGE"
        },
        {
            "index": 4,
            "company": "MAINELAND"
        }
    ]
    for company in company_data:
        Company.objects.create(**company)

def pre_load_foods():
    food_data = [
        {
            "id": uuid.uuid4(),
            "type": "Fruit",
            "name": 'orange'
        },
        {
            "id": uuid.uuid4(),
            "type": "Vegetable",
            "name": 'beetroot'
        },
        {
            "id": uuid.uuid4(),
            "type": "Fruit",
            "name": 'strawberry'
        },
        {
            "id": uuid.uuid4(),
            "type": "Vegetable",
            "name": 'cucumber'
        },
        {
            "id": uuid.uuid4(),
            "type": "Vegetable",
            "name": 'celery'
        },
        {
            "id": uuid.uuid4(),
            "type": "Fruit",
            "name": 'banana'
        },
        {
            "id": uuid.uuid4(),
            "type": "Vegetable",
            "name": 'carrot'
        },
        {
            "id": uuid.uuid4(),
            "type": "Fruit",
            "name": 'apple'
        }
    ]
    for food in food_data:
        Food.objects.create(**food)

def pre_load_tags():
    tag_data = [
        {"name": "nostrud"},
        {"name": "non"},
        {"name": "commodo"},
        {"name": "duis"},
        {"name": "sit"},
        {"name": "labore"},
        {"name": "occaecat"}
    ]
    for tag in tag_data:
        Tag.objects.create(**tag)

def pre_load_people():
    people1 = {
            "_id": "595eeb9b96d80a5bc7afb106",
            "index": 0,
            "guid": "5e71dc5d-61c0-4f3b-8b92-d77310c7fa43",
            "has_died": True,
            "balance": Decimal("$2,418.59".strip('$').replace(',', '')),
            "picture": "http://placehold.it/32x32",
            "age": 61,
            "eye_color": "blue",
            "name": "Carmella Lambert",
            "gender": "female",
            "company_id": 1,
            "email": "carmellalambert@earthmark.com",
            "phone": "+1 (910) 567-3630",
            "address": "628 Sumner Place, Sperryville, American Samoa, 9819",
            "about": "Non duis dolore ad enim. Est id reprehenderit cupidatat tempor excepteur. Cupidatat labore incididunt nostrud exercitation ullamco reprehenderit dolor eiusmod sit exercitation est. Voluptate consectetur est fugiat magna do laborum sit officia aliqua magna sunt. Culpa labore dolore reprehenderit sunt qui tempor minim sint tempor in ex. Ipsum aliquip ex cillum voluptate culpa qui ullamco exercitation tempor do do non ea sit. Occaecat laboris id occaecat incididunt non cupidatat sit et aliquip.\r\n",
            "registered": "2016-07-13T12:29:07 -10:00",
            "friends": "2,3,4,5",
            "greeting": "Hello, Carmella Lambert! You have 6 unread messages.",
        }
    people1['registered'] = dateutil.parser.parse(people1['registered'])
    people1 = People.objects.create(**people1)
    people1.tags.add(Tag.objects.get(name='nostrud'))
    people1.tags.add(Tag.objects.get(name='nostrud'))
    people1.favourite_foods.add(Food.objects.get(name='apple'))
    people1.favourite_foods.add(Food.objects.get(name='banana'))
    people1.favourite_foods.add(Food.objects.get(name='carrot'))
    people1.save()

    people2 = {
            "_id": "595eeb9b1e0d8942524c98ad",
            "index": 1,
            "guid": "b057bb65-e335-450e-b6d2-d4cc859ff6cc",
            "has_died": False,
            "balance": Decimal("$1,562.58".strip('$').replace(',', '')),
            "picture": "http://placehold.it/32x32",
            "age": 60,
            "eye_color": "brown",
            "name": "Decker Mckenzie",
            "gender": "male",
            "company_id": 2,
            "email": "deckermckenzie@earthmark.com",
            "phone": "+1 (893) 587-3311",
            "address": "492 Stockton Street, Lawrence, Guam, 4854",
            "about": "Consectetur aute consectetur dolor aliquip dolor sit id. Sint consequat anim occaecat ad mollit aliquip ut aute eu culpa mollit qui proident eu. Consectetur ea et sit exercitation aliquip officia ea aute exercitation nulla qui sunt labore. Enim veniam labore do irure laborum aute exercitation consectetur. Voluptate adipisicing velit sunt consectetur id sint adipisicing elit elit pariatur officia amet officia et.\r\n",
            "registered": "2017-06-25T10:03:49 -10:00",
            "greeting": "Hello, Decker Mckenzie! You have 2 unread messages.",
            "friends": "3,4,5"
          }
    people2['registered'] = dateutil.parser.parse(people2['registered'])
    people2 = People.objects.create(**people2)
    people2.tags.add(Tag.objects.get(name='commodo'))
    people2.favourite_foods.add(Food.objects.get(name='beetroot'))
    people2.favourite_foods.add(Food.objects.get(name='banana'))
    people2.save()

    people3 = {
        "_id": "595eeb9bb3821d9982ea44f9",
        "index": 2,
        "guid": "49c04b8d-0a96-4319-b310-d6aa8269adca",
        "has_died": False,
        "balance": Decimal("$2,119.44".strip('$').replace(',', '')),
        "picture": "http://placehold.it/32x32",
        "age": 54,
        "eye_color": "brown",
        "name": "Bonnie Bass",
        "gender": "female",
        "company_id": 4,
        "email": "bonniebass@earthmark.com",
        "phone": "+1 (823) 428-3710",
        "address": "455 Dictum Court, Nadine, Mississippi, 6499",
        "about": "Non voluptate reprehenderit ad elit veniam nulla ut ea ex. Excepteur exercitation aliquip Lorem nisi duis. Ex cillum commodo labore sint non velit aliquip cupidatat sint. Consequat est sint do in eiusmod minim exercitation do consectetur incididunt culpa deserunt. Labore veniam elit duis minim magna et laboris sit labore eu velit cupidatat cillum cillum.\r\n",
        "registered": "2017-06-08T04:23:18 -10:00",
        "greeting": "Hello, Bonnie Bass! You have 10 unread messages.",
        "friends": "4"
    }

    people3['registered'] = dateutil.parser.parse(people3['registered'])
    people3 = People.objects.create(**people3)
    people3.tags.add(Tag.objects.get(name='commodo'))
    people3.favourite_foods.add(Food.objects.get(name='beetroot'))
    people3.save()

    people4 =  {
            "_id": "595eeb9bfa3a6e19be68df9e",
            "index": 3,
            "guid": "64d71744-1af5-46fd-84bc-4bf37c193b2d",
            "has_died": True,
            "balance": Decimal("$3,453.69".strip('$').replace(',', '')),
            "picture": "http://placehold.it/32x32",
            "age": 30,
            "eye_color": "blue",
            "name": "Rosemary Hayes",
            "gender": "female",
            "company_id": 4,
            "email": "rosemaryhayes@earthmark.com",
            "phone": "+1 (984) 437-3226",
            "address": "130 Bay Parkway, Marshall, Virgin Islands, 298",
            "about": "Enim velit irure adipisicing eiusmod cillum ullamco culpa incididunt mollit nisi ea irure. Ut cupidatat nostrud ipsum non. Labore quis elit aliqua veniam duis amet minim dolor tempor culpa cillum magna sint velit.\r\n",
            "registered": "2015-04-22T03:36:03 -10:00",
            "greeting": "Hello, Rosemary Hayes! You have 1 unread messages.",
            "friends": '1,5'
    }
    people4['registered'] = dateutil.parser.parse(people4['registered'])
    people4 = People.objects.create(**people4)
    people4.tags.add(Tag.objects.get(name='commodo'))
    people4.favourite_foods.add(Food.objects.get(name='beetroot'))
    people4.save()

    people5 = {
            "_id": "595eeb9b309724177239a445",
            "index": 4,
            "guid": "b4ec861a-7b57-4830-bf46-140135123549",
            "has_died": False,
            "balance": Decimal("$3,453.69".strip('$').replace(',', '')),
            "picture": "http://placehold.it/32x32",
            "age": 62,
            "eye_color": "blue",
            "name": "Mindy Beasley",
            "gender": "female",
            "email": "mindybeasley@earthmark.com",
            "phone": "+1 (862) 503-2197",
            "address": "628 Brevoort Place, Bellamy, Kansas, 2696",
            "about": "Et consequat mollit occaecat in eiusmod ipsum ad magna. Labore aliquip ut in amet. Non ullamco ea reprehenderit cupidatat voluptate duis ullamco duis ut. Amet et nostrud dolore in amet eiusmod ullamco commodo nulla. Commodo quis commodo proident elit aliquip. Sunt nostrud mollit nostrud cupidatat do officia enim eu ut id excepteur.\r\n",
            "registered": "2017-03-19T03:28:28 -11:00",
            "greeting": "Hello, Mindy Beasley! You have 8 unread messages."
    }

    people5['registered'] = dateutil.parser.parse(people5['registered'])
    people5 = People.objects.create(**people5)
    people5.tags.add(Tag.objects.get(name='commodo'))
    people5.favourite_foods.add(Food.objects.get(name='banana'))
    people5.save()

    people6 = {
            "_id": "595eeb9b82faeaf4b3274529",
            "index": 5,
            "guid": "a5c37a3d-3e0d-4aba-adc5-51cf83283611",
            "has_died": False,
            "balance": Decimal("$3,453.69".strip('$').replace(',', '')),
            "picture": "http://placehold.it/32x32",
            "age": 24,
            "eye_color": "brown",
            "name": "Grace Kelly",
            "gender": "female",
            "company_id": 4,
            "email": "gracekelly@earthmark.com",
            "phone": "+1 (923) 600-2868",
            "address": "762 Tabor Court, Ola, Idaho, 4329",
            "about": "Amet velit do non voluptate Lorem in nostrud anim officia. Cupidatat nostrud sit reprehenderit consequat aute est reprehenderit eu nostrud. Labore ad exercitation ad non.\r\n",
            "registered": "2016-12-31T12:45:45 -11:00",
            "greeting": "Hello, Grace Kelly! You have 4 unread messages.",
        }

    people6['registered'] = dateutil.parser.parse(people6['registered'])
    people6 = People.objects.create(**people6)
    people6.tags.add(Tag.objects.get(name='commodo'))
    people6.favourite_foods.add(Food.objects.get(name='beetroot'))
    people6.save()


class ApiTestCase(TestCase):
    """"""
    def setUp(self):
        self.client = APIClient()
        pre_load_companies()
        pre_load_foods()
        pre_load_tags()
        pre_load_people()

    def test_company_not_found_by_id(self):
        """test comapny not found by input company id"""
        url = reverse("paranuara:company_employees", kwargs={'company_id': 1000})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_company_without_employee(self):
        """test company with no employees"""
        url = reverse("paranuara:company_employees", kwargs={'company_id': 3})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_company_add_employee(self):
        """test for company with no employees, add a new employee for the company"""
        new_employee = {
            "name": "ran jing",
            "age": 34,
            "has_died": False,
            "eye_color": "black",
            "gender": "male",
            "email": "test@gmail.com",
            "phone": "+1 (842) 598-352594",
            "address": "melbourne cbd",
            "greeting": "hello",
            "company": Company.objects.get(index=3)
        }

        url = reverse("paranuara:add_employee", kwargs={'company_id': 3})
        serializer = EmployeesSerializer(data=new_employee)
        if serializer.is_valid():
            res = self.client.post(url, data=serializer.data)
            self.assertEqual(res.status_code, status.HTTP_201_CREATED)
            url = reverse("paranuara:company_employees", kwargs={'company_id': 3})
            res = self.client.get(url)
            self.assertEqual(res.status_code, status.HTTP_200_OK)
            self.assertEqual(len(res.data), 1)

    def test_company_employees(self):
        """test for company employees"""
        url = reverse("paranuara:company_employees", kwargs={'company_id': 1})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(len(res.data), 1)

    def test_people_not_found_by_id(self):
        """test for searching people failed"""
        url = reverse("paranuara:favourite_foods", kwargs={'pk1': 10})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_404_NOT_FOUND)

    def test_people_favourite_food(self):
        """test for listing people favourite food"""
        url = reverse("paranuara:favourite_foods", kwargs={'pk1': 0})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(res.data['fruits'])
        self.assertIsNotNone(res.data['vegetables'])

    def test_people_with_mutual_friends(self):
        """test for people with mutual alive brown eyes friends"""
        url = reverse("paranuara:mutual_friends", kwargs={'pk1':0, 'pk2':1})
        res = self.client.get(url)
        self.assertIsNotNone(res.data['person1'])
        self.assertIsNotNone(res.data['person2'])
        self.assertEqual(len(res.data['mutual_friends']), 1)
        self.assertEqual(res.data['mutual_friends'][0]['name'], 'Grace Kelly')

    def test_people_without_mutual_friends(self):
        """test for people without mutual alive brown eyes friends"""
        url = reverse("paranuara:mutual_friends", kwargs={'pk1': 2, 'pk2': 3})
        res = self.client.get(url)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertIsNotNone(res.data['person1'])
        self.assertIsNotNone(res.data['person2'])
        self.assertEqual(len(res.data['mutual_friends']), 0)
