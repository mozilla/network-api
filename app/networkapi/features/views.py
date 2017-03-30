from rest_framework.generics import ListAPIView, RetrieveAPIView

from networkapi.features.models import Feature
from networkapi.features.serializers import FeatureSerializer


class FeatureListView(ListAPIView):
    """
    A view that permits a GET to allow listing of Features
    in the database
    """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
    pagination_class = None


class FeatureView(RetrieveAPIView):
    """
    A view that permits a GET request for an Feature in the database
    """
    queryset = Feature.objects.all()
    serializer_class = FeatureSerializer
