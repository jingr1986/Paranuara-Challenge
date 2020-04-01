from django.contrib import admin
from .models import Company, People, Tag, Food

admin.site.register(Company)
admin.site.register(People)
admin.site.register(Tag)
admin.site.register(Food)