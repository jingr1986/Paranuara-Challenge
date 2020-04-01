from rest_framework import status, viewsets, views
from rest_framework.response import Response
from rest_framework.exceptions import ValidationError
from django.urls import reverse

from .models import People, Company
from . import serializers

class EmployeesView(viewsets.ModelViewSet):
    """
    Given a company index returns all its employees.
    """
    queryset = People.objects.all()
    serializer_class = serializers.EmployeesSerializer

    def list(self, request, company_id, *args, **kwargs):
        """"""
        company = Company.objects.filter(index=company_id)
        employees = People.objects.filter(company__in=company)
        serializer = serializers.PeopleInfoSerializer(employees, many=True)
        if len(serializer.data) == 0:
            return Response({'msg': 'No employee in this company',
                             'new employee': reverse("paranuara:add_employee", kwargs={'company_id': company_id})},
                            status = status.HTTP_404_NOT_FOUND)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, company_id):
        if request.data:
            try:
                serializer = serializers.EmployeesSerializer(data=request.data)
                serializer.is_valid(raise_exception=True)
                serializer.save()
                return Response({'status': 'New employee added'}, status=status.HTTP_201_CREATED)
            except ValidationError as e:
                return Response({'error': filter(None, e.detail)}, status=status.HTTP_400_BAD_REQUEST)
        return Response({'status': 'Data not found'}, status=status.HTTP_204_NO_CONTENT)


class MutualFriendsView(views.APIView):
    """given two people's index, return their mutual alive brown eyes friend"""

    def get(self, request, pk1, pk2, *args, ** kwargs):

        if pk1>=0 and pk2>=0:
            people = People.objects.filter(index__in=(pk1, pk2))
            if people.count() != 2:
                return Response({'msg': 'people not found'}, status = status.HTTP_404_NOT_FOUND)
            friends1 = people[0].friends.split(',')
            friends2 = people[1].friends.split(',')
            mutual_friends = list(set(friends1).intersection(friends2))
            mutual_friends = People.objects.filter(index__in=mutual_friends, eye_color='brown', has_died=False)
            payload = {
                'people1': people[0],
                'people2': people[1],
                'mutual_friends': mutual_friends
            }
            serializer = serializers.MutualFriendsSerializer(payload)
            return Response(serializer.data)
        else:
            return Response({'msg': 'invalid parameters'}, status=status.HTTP_400_BAD_REQUEST)

class FavouriteFoodsView(views.APIView):
    """given a people's id return peopel's favourite food"""

    def get(self, request, pk1, *args, ** kwargs):
        """"""
        people = People.objects.filter(index=pk1)
        if people:
            serializer = serializers.FavouriteFoodsSerializer(people, many=True)
            return Response(serializer.data[0], status=status.HTTP_200_OK)
        else:
            return Response({'msg': 'people not found'}, status = status.HTTP_404_NOT_FOUND)
