
import uuid
import datetime
import ast
from django.db import models


def convert_str_to_datetime(s):
    """
    Convert str to datetime
    :param s: str ex: "31/12/2020T12:40:00.000Z"
    :return: datetime
    """

    try:
        return datetime.datetime.strptime(s, "%Y-%m-%dT%H:%M:%S.000Z")

    except Exception:
        return None


def parse_str(s):
    """
    parse str to int or float
    :param s: number in str
    :return: datetime
    """

    try:
        return ast.literal_eval(str(s))
    except:
        return None


class BaseModel(models.Model):
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created_at = models.DateTimeField(blank=True, null=True, db_index=True)
    updated_at = models.DateTimeField(blank=True, null=True, db_index=True)

    class Meta:
        abstract = True

    def get_id(self):
        return self.id.__str__()
