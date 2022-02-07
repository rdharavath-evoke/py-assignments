from import_export import resources
from .models import Xref

class XrefResource(resources.ModelResource):
    class meta:
        model=Xref