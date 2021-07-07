from django.contrib import admin
from cars.models import CarDetail

class CarDetailAdminConfig(admin.ModelAdmin):
    search_fields=['name','company','car_type','transmission_type']
    list_display = ('company','id','name','price','transmission_type','model_year','inventory')

admin.site.register(CarDetail, CarDetailAdminConfig )

