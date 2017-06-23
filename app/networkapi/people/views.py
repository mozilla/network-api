from rest_framework.generics import ListAPIView, RetrieveAPIView

from networkapi.people.models import Person
from networkapi.people.serializers import PersonSerializer


class PeopleListView(ListAPIView):
    """
    A view that permits a GET to allow listing all the People
    in the database
    """
    queryset = Person.objects.published()

    # What is actually going on at the DB level?
    # see https://docs.djangoproject.com/en/1.11/ref/models/expressions
    db = queryset.db
    compiler = queryset.query.get_compiler(using=db)
    sql = compiler.as_sql()
    print("template tuple:\n", sql)
    print("template result:\n", sql[0] % sql[1])

    serializer_class = PersonSerializer


class PersonView(RetrieveAPIView):
    """
    A view that permits a GET to allow listing a person
    in the database
    """
    queryset = Person.objects.published()
    serializer_class = PersonSerializer
