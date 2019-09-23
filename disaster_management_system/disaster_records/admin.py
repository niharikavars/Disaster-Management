from django.contrib import admin

# Register your models here.
from .models import DisasterRecords

admin.site.register(DisasterRecords)

from .models import EmergencyContactInfo

admin.site.register(EmergencyContactInfo)

from .models import Relief_fund

admin.site.register(Relief_fund)

from .models import AffectedData

admin.site.register(AffectedData)


