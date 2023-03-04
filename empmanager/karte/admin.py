from django.contrib import admin
from .models import Pain, Range, RehaPlan, Comment, KarteInfo

# Register your models here.
admin.site.register(Pain)
admin.site.register(Range)
admin.site.register(RehaPlan)
admin.site.register(Comment)
admin.site.register(KarteInfo)