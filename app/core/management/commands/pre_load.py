import json, os, dateutil
import pandas as pd
from itertools import chain
from django.core.management.base import BaseCommand, CommandError
from core.serializers import CompanySerializer, TagSerializer, FoodSerializer
from core.models import People, Company, Tag, Food
from decimal import Decimal

FILE_PATH = './static'

class Command(BaseCommand):
    """Sets up database with resouces data."""

    def read_json_file(self, file_path):
        """Reads a JSON file from file path."""
        try:
            with open(file_path) as json_file:
                return json.load(json_file)
        except OSError:
            raise CommandError(f'can not open {file_path}.')

    def to_db(self, serializer, type):
        """use serializer to save data to db"""
        if serializer.is_valid():
            serializer.save()
            self.stdout.write(self.style.SUCCESS(f'load {type} success !'))
        else:
            self.stdout.write(self.style.NOTICE(f'{type} data is invalid !'))
            self.stdout.write(serializer.errors)

    def load_companies(self):
        """load the company data"""
        file = os.path.join('./resources/', 'companies.json')
        data = self.read_json_file(file)
        serializer = CompanySerializer(data=data, many=True)
        self.to_db(serializer, 'company')

    def load_people_detail(self):
        """load all the residents and save to db"""
        file = os.path.join('./resources/', 'people.json')
        data = pd.read_json(file)

        # load tags
        tags = [{'name': x} for x in list(set(chain(*data.tags.values)))]
        self.to_db(TagSerializer(data=tags, many=True), 'Tag')

        # # load foods
        foods = [{'name': x} for x in list(set(chain(*data.favouriteFood.values)))]
        self.to_db(FoodSerializer(data=foods, many=True), 'Food')

        # load people
        json_data = self.read_json_file(file)
        for data in json_data:
            resident = People()
            resident._id = data['_id']
            resident.guid = data['guid']
            resident.index = data['index']
            resident.name = data['name']
            resident.age = data['age']
            resident.has_died = False if data['has_died'] == "false" or data['has_died'] == False else True
            resident.balance = Decimal(data['balance'].strip('$').replace(',', ''))
            resident.picture = data['picture']
            resident.eye_color = data['eyeColor']
            resident.gender = data['gender']
            resident.company = Company.objects.get(index=data['company_id']-1)
            resident.email = data['email']
            resident.phone = data['phone']
            resident.address = data['address']
            resident.about = data['about']
            resident.registered = dateutil.parser.parse(data['registered'])

            resident.save()

            tags = data.pop('tags') if 'tags' in data else None
            if tags:
                for value in tags:
                    resident.tags.add(Tag.objects.get(name=value))
                resident.save()

            favourite_foods = data.pop('favouriteFood') if 'favouriteFood' in data else None
            if favourite_foods:
                for food in favourite_foods:
                    resident.favourite_foods.add(Food.objects.get(name=food))
                resident.save()

            friends = data.pop('friends') if 'friends' in data else None
            if friends:
                resident.friends = ','.join(str(friend['index']) for friend in friends)
                resident.save()

        self.stdout.write(self.style.SUCCESS('load people success !'))

    def clear_db(self):
        """clear the data in db when start load data"""
        People.objects.all().delete()
        Company.objects.all().delete()
        Tag.objects.all().delete()
        Food.objects.all().delete()
        self.stdout.write(self.style.SUCCESS('Successfully cleared all data'))

    def handle(self, *args, **options):
        self.stdout.write(self.style.WARNING('Start to clear db ...'))
        self.clear_db()
        self.stdout.write(self.style.WARNING('Start to load company ...'))
        self.load_companies()
        self.stdout.write(self.style.WARNING('Start to load people ...'))
        self.load_people_detail()