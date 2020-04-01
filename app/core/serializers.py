from rest_framework import serializers
from .models import Company, People, Tag, Food

class CompanySerializer(serializers.ModelSerializer):
    """serializer for Company objects"""

    class Meta:
        model = Company
        fields = ('index', 'company')

class PeopleInfoSerializer(serializers.ModelSerializer):
    """serializer for people brief info objects"""
    class Meta:
        model = People
        fields = ('name', 'age', 'address', 'phone',)

class EmployeesSerializer(serializers.ModelSerializer):
    """serializer for adding a new employee objects"""
    name = serializers.CharField(max_length=255)
    age = serializers.IntegerField(default=1)
    has_died = serializers.BooleanField(default=False)
    eye_color = serializers.CharField(max_length=32)
    gender = serializers.CharField(max_length=10)
    email = serializers.EmailField(max_length=255)
    phone = serializers.CharField(max_length=255)
    address = serializers.CharField(max_length=255)
    greeting = serializers.CharField(max_length=255)
    company = serializers.PrimaryKeyRelatedField(queryset=Company.objects.all())

    class Meta:
        model = People
        fields = ('name', 'age', 'has_died', 'eye_color', 'gender', 'email', 'phone', 'address', 'greeting', 'company')

    def create(self, validated_data):
        return People.objects.create(**validated_data)

class TagSerializer(serializers.ModelSerializer):
    """serializer for tag objects"""
    class Meta:
        model = Tag
        fields = ('name',)

class MutualFriendsSerializer(serializers.ModelSerializer):
    """serializer for getting mutual alive brown eyes friend object"""
    class Meta:
        model = People
        fields = ('people1', 'people2', 'mutual_friends')

    def to_representation(self, obj):
        return {
            'person1': PeopleInfoSerializer(obj['people1']).data,
            'person2': PeopleInfoSerializer(obj['people2']).data,
            'mutual_friends': PeopleInfoSerializer(obj['mutual_friends'], many=True).data,
        }

class FoodSerializer(serializers.ModelSerializer):
    """serializer for food object """
    food_types = {
        'orange': 'Fruit',
        'beetroot': 'Vegetable',
        'strawberry': 'Fruit',
        'cucumber': 'Vegetable',
        'celery': 'Vegetable',
        'banana': 'Fruit',
        'carrot': 'Vegetable',
        'apple': 'Fruit',
    }

    class Meta:
        model = Food
        fields = ('name',)

    def create(self, validated_data):
        name = validated_data['name']
        validated_data['type'] = self.food_types[name] if name in self.food_types.keys() else 'Unknown'
        return Food.objects.create(**validated_data)


class FavouriteFoodsSerializer(serializers.ModelSerializer):
    """serializer for display people's favourite food object """
    username = serializers.CharField(source='name')
    fruits = serializers.SerializerMethodField('get_fruits')
    vegetables = serializers.SerializerMethodField('get_vegs')

    class Meta:
        model = People
        fields = ('username', 'age', 'fruits', 'vegetables',)
        read_only_fields = ('username', 'age', 'fruits', 'vegetables',)

    def get_fruits(self, obj):
        """"""
        return obj.favourite_foods.filter(type__exact='Fruit').values_list('name', flat=True)

    def get_vegs(self, obj):
        """"""
        return obj.favourite_foods.filter(type__exact='Vegetable').values_list('name', flat=True)



