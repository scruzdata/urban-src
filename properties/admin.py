from django.contrib import admin

# Register your models here.
from django.contrib.gis import admin
from rangefilter.filters import DateRangeFilter
from django_admin_listfilter_dropdown.filters import ChoiceDropdownFilter, DropdownFilter
from properties.models import Property


@admin.register(Property)
class PropertyAdmin(admin.OSMGeoAdmin):
    list_display = ('id_uda', 'boundary_id', 'property_type', 'date_in', 'date_out', 'is_active', 'date_in', 'date_out')
    search_fields = ('id_uda',)
    list_filter = (
        ('id_uda', DropdownFilter),
        ('property_type', ChoiceDropdownFilter),
        ('date_in', DateRangeFilter),
        ('date_out', DateRangeFilter),
    )
    ordering = ('-created_at',)