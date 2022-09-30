

from django.contrib.gis.db.models.functions import GeometryDistance
from django.contrib.gis.geos import Point
from rest_framework import viewsets, mixins, status
from rest_framework.response import Response

from properties.models import Property
from properties.serializers import PropertySerializer
from utils.helpers import parse_str


class RetailsViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def list(self, request, *args, **kwargs):
        try:

            id_uda = request.GET.get("id_uda", None)
            kwargs = {}
            if id_uda:
                kwargs = {'id_uda': id_uda}

            try:
                properties = Property.objects.filter(**kwargs)
            except Property.DoesNotExist:
                return Response({
                    'result': 'ERROR',
                    'detail': f'Property does not exist for that id_uda: {id_uda}'
                }, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                'result': 'OK',
                'detail': f'Property succesfully listed!',
                'results': PropertySerializer(properties, many=True).data
            }, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response({
                'result': 'ERROR',
                'detail': ex.__str__()
            }, status=status.HTTP_400_BAD_REQUEST)


class PropertyByDistanceAndCoordinatesViewSet(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Property.objects.all()
    serializer_class = PropertySerializer

    def list(self, request, *args, **kwargs):
        try:

            distance = request.GET.get('distance', 0)
            if not distance:
                return Response({
                    'result': 'ERROR',
                    'detail': 'distance is missing or empty'
                }, status=status.HTTP_400_BAD_REQUEST)

            distance = parse_str(distance)
            distance_km = distance * 1000

            latitude = request.GET.get('latitude', 0)
            longitude = request.GET.get('longitude', 0)
            if not latitude:
                return Response({
                    'result': 'ERROR',
                    'detail': 'latitude is required (latitude=40.000)',
                }, status=status.HTTP_400_BAD_REQUEST)
            if not longitude:
                return Response({
                    'result': 'ERROR',
                    'detail': 'longitude is required (longitude=-3.000)',
                }, status=status.HTTP_400_BAD_REQUEST)

            try:
                latitude = parse_str(latitude)
                longitude = parse_str(longitude)
                if not latitude or not longitude:
                    return Response({
                        'result': 'ERROR',
                        'detail': 'coordinates is required (latitude=40.000&longitude=-37.000)',
                    }, status=status.HTTP_400_BAD_REQUEST)
            except Exception:
                return Response({
                    'result': 'ERROR',
                    'detail': 'coordinates is required (latitude=40.000&longitude=-37.000)',
                }, status=status.HTTP_400_BAD_REQUEST)

            pnt = Point(longitude, latitude, srid=4326)

            try:
                properties = Property.objects.annotate(distance=GeometryDistance("coordinates", pnt)).filter(distance__lte=distance_km).order_by('distance')
            except Property.DoesNotExist:
                return Response({
                    'result': 'ERROR',
                    'detail': f'Property does not exist'
                }, status=status.HTTP_400_BAD_REQUEST)

            return Response({
                'result': 'OK',
                'detail': f'Properties within {distance} kilometers of Coordinate {latitude,longitude} succesfully listed!',
                'results': PropertySerializer(properties, many=True).data
            }, status=status.HTTP_200_OK)

        except Exception as ex:
            return Response({
                'result': 'ERROR',
                'detail': ex.__str__()
            }, status=status.HTTP_400_BAD_REQUEST)
