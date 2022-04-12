import datetime
from django.utils import timezone
class Properties:
    def __init__(self):
        self.EXCEPTION="EXCEPTION"
        self.SUCCESS="SUCCESS"
        self.FAILED="FAILED"
        self.STATUS="STATUS"
        self.DATA="DATA"
        self.DESCRIPTION="DESCRIPTION"
        self.OBJECT_NOT_FOUND="OBJECT_NOT_FOUND"
        self.date_format=r"%m/%d/%Y"
    @staticmethod    
    def dict_clean(items):
        result = {}
        for key, value in items.items():
            if value is None:
                value = ''
            result[key] = value
        return result
    @staticmethod
    def get_date_time():
        return timezone.now()
class TransactionException(Exception):
    pass