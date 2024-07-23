from django.db import models

# see https://docs.djangoproject.com/en/1.5/ref/models/fields/#field-types
# Create your models here.

# Django names the table or collection automatically as myapp_super, myapp_sub
# A Super has many Subs


class Super(models.Model):
    name = models.CharField(max_length=20)
    code = models.IntegerField(default=1)

    class Meta:  # all querysets will be "ORDER BY name DESC, code ASC"
        ordering = ['-name', 'code']

    def __str__(self):   # String representation for an album used by e.g. print() command
        return f"PK: {self.pk}, Name: {self.name}, Code: {self.code}"

class Sub(models.Model):
    super = models.ForeignKey(Super,on_delete=models.CASCADE) #foreign key must exist if Super deleted all of subs also will delete
    sub_name = models.CharField(max_length=20)
    def __str__(self):
        return f"PK: {self.pk}, Sub_Name: {self.sub_name},"






#  ForeignKey(unique=True) is usually better served by a OneToOneField.

from django.db import models

class Engine(models.Model):
    name = models.CharField(max_length=25)
    def __str__(self):
        return f'Engine={self.name}'
class Car(models.Model):
    name = models.CharField(max_length=25)
    engine = models.OneToOneField(Engine, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Car={self.name}'

class Engine2(models.Model):
    name = models.CharField(max_length=25, null=True)
    def __str__(self):
        return f'Engine={self.name}'

class Car2(models.Model):
    name = models.CharField(max_length=25)
    engine = models.ForeignKey(Engine2, unique=True, on_delete=models.SET_NULL, null=True)
    def __str__(self):
        return f'Car={self.name}'


# OneToOneField Example
# >>> from testapp.models import Car, Engine, Car2, Engine2

# >>> Engine.objects.create(name='Diesel')
# >>> Engine.objects.create(name='Gas')
# >>> Engine2.objects.create(name='Diesel')
# >>> Engine2.objects.create(name='Gas')
# >>> Car.objects.create(name='Mazda', engine_id=1)
# >>> Car.objects.create(name='Honda', engine_id=2)
# >>> Car2.objects.create(name='Mazda', engine_id=1)
# >>> Car2.objects.create(name='Honda', engine_id=2)


# >>> c = Car.objects.get(name='Mazda')
# >>> e = Engine.objects.get(name='Diesel')
# >>> e.car
# <Car: Car=Mazda>

# >>> c2 = Car2.objects.get(name='Mazda')
# >>> e2 = Engine2.objects.get(name='Wankel')
# >>> e2.car2_set.all()
# >>> : <QuerySet [<Car2: Car=Mazda>]>
