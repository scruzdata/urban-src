from rest_framework import serializers

from properties.models import Property


class PropertySerializer(serializers.ModelSerializer):

    class Meta:
        model = Property
        fields = ('id', 'id_uda', 'boundary_id',
                  'title', 'description', 'coordinates',
                  'build_status', 'is_active',
                  'date_in', 'date_out', 'date_diff',
                  'start_month', 'end_month',
                  'start_week', 'end_week',
                  'start_quarter', 'end_quarter',
                  'construction_type', 'property_type', 'typology_type', 'listing_type',
                  'last_activity')
