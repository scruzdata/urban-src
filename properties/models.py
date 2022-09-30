from django.db import models

# Create your models here.
from django.contrib.gis.db import models

from utils.constans import PROPERTY_TYPES, PROPERTY_TYPE_1_ID
from utils.helpers import BaseModel


class Property(BaseModel):
    build_status = models.IntegerField(blank=True, null=True)
    is_active = models.BooleanField(default=True)
    start_month = models.IntegerField(blank=True, null=True)
    construction_type = models.IntegerField(blank=True, null=True)
    date_diff = models.IntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    date_in = models.DateTimeField(blank=True, null=True)
    property_type = models.PositiveSmallIntegerField(choices=PROPERTY_TYPES, default=PROPERTY_TYPE_1_ID)
    end_week = models.IntegerField(blank=True, null=True)
    typology_type = models.IntegerField(blank=True, null=True)
    coordinates = models.PointField(srid=4326, geography=True, null=True, blank=True)
    boundary_id = models.IntegerField(blank=True, null=True)
    id_uda = models.CharField(max_length=100, blank=True, null=True)
    title = models.CharField(max_length=100, blank=True, null=True)
    listing_type = models.IntegerField(blank=True, null=True)
    date_out = models.DateTimeField(blank=True, null=True)
    start_week = models.IntegerField(blank=True, null=True)
    end_quarter = models.IntegerField(blank=True, null=True)
    last_activity = models.IntegerField(blank=True, null=True)
    start_quarter = models.IntegerField(blank=True, null=True)
    end_month = models.IntegerField(blank=True, null=True)

    def __str__(self):
        return f'id_uda:{self.id_uda}-Title:{self.title}' if self.title else f'id_uda:{self.id_uda}'

    class Meta:
        verbose_name = 'Property'
        verbose_name_plural = 'Properties'
        db_table = 'properties'
        unique_together = ('id_uda', 'title')