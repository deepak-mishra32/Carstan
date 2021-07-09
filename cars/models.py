from django.db import models
from django.utils.translation import gettext_lazy as _
from multiselectfield import MultiSelectField

CAR_TYPES = (('Hatchback', 'Hatchback'),
               ('Sedan', 'Sedan'),
               ('SUV', 'SUV'),
               ('Luxury', 'Luxury'))
            
TRANSMISSION_TYPES=(('Automatic','Automatic'),
                    ('Manual','Manual'))

MODEL_YEARS=(('2010-2012','2010-2012'),
            ('2013-2016','2013-2016'),
            ('2017-2019','2017-2019'),
            ('2020-2021','2020-2021'))

FUEL_TYPE=(('Petrol','Petrol'),
            ('Diesel','Diesel'),
            ('CNG','CNG'),
            ('Electric','Electric'))

class CarDetail(models.Model):
    car_type=MultiSelectField(_('Category'),choices=CAR_TYPES,max_choices=2,blank=False,null=False)
    company=models.CharField(_('Company'),max_length=156, blank= False, null=False,default=None)
    name=models.CharField(_('Name'),max_length=156, blank= False, null=False)
    model_year=MultiSelectField(_('Model'),choices=MODEL_YEARS,max_choices=2,blank=False,null=False)
    transmission_type=MultiSelectField(_('Transmission'),choices=TRANSMISSION_TYPES,max_choices=2,blank=False,null=False)
    fuel_type=MultiSelectField(_('Fuel'),choices=FUEL_TYPE,max_choices=2,blank=False,null=False)
    price=models.FloatField(_('Price (in lakhs)'), blank= False, null=False)
    detail=models.CharField(_("Description"),max_length=2000,blank=True,null=True,default=None)
    inventory=models.IntegerField(_("Stock"), blank= False, null=False,default=None)
    image1=models.ImageField(_("Image1"), upload_to='cars', height_field=None, width_field=None, max_length=None,blank= True, null=True)
    image2=models.ImageField(_("Image2"), upload_to='cars', height_field=None, width_field=None, max_length=None,blank= True, null=True)
    image3=models.ImageField(_("Image3"), upload_to='cars', height_field=None, width_field=None, max_length=None,blank= True, null=True)
    image4=models.ImageField(_("Image4"), upload_to='cars', height_field=None, width_field=None, max_length=None,blank= True, null=True)


    def __str__(self):
        return self.name