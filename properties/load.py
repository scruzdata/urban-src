import csv
from pathlib import Path
from django.utils import timezone

from django.contrib.gis.geos import Point


from utils.helpers import parse_str, convert_str_to_datetime
from .models import Property


assest_file = Path(__file__).resolve().parent / "assets.csv"


def run():
    # optional to delete is data saved
    Property.objects.all().delete()

    now = timezone.now()
    with open(assest_file, encoding='utf-8') as csv_file:
        heading = next(csv_file)

        # Create reader object by passing the file
        reader_obj = csv.reader(csv_file)

        # Iterate over each row in the csv file
        properties = []
        for record in reader_obj:
            latitude = None
            longitude = None
            if record:
                coordinates = record[11].split(',') if record[11] else None
                if coordinates:
                    latitude = parse_str(coordinates[0])
                    longitude = parse_str(coordinates[1])
                properties.append(
                    Property(
                        build_status=parse_str(record[0]),
                        is_active=record[1],
                        start_month=parse_str(record[2]),
                        construction_type=parse_str(record[3]),
                        date_diff=parse_str(record[4]),
                        description=str(record[5]),
                        date_in=convert_str_to_datetime(record[6]),
                        property_type=parse_str(record[7]),
                        end_week=parse_str(record[8]),
                        typology_type=parse_str(record[9]),
                        id=parse_str(record[10]),
                        coordinates=Point(longitude, latitude),
                        boundary_id=parse_str(record[12]),
                        id_uda=str(record[13]),
                        title=str(record[14]),
                        listing_type=parse_str(record[15]),
                        date_out=convert_str_to_datetime(record[16]),
                        start_week=parse_str(record[17]),
                        end_quarter=parse_str(record[18]),
                        last_activity=parse_str(record[19]),
                        start_quarter=parse_str(record[20]),
                        end_month=parse_str(record[21]),
                        created_at=now))

        if properties:
            Property.objects.bulk_create(properties)
        print(f">> Properties already saved!")
