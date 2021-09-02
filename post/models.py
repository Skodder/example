from django.db import models


class Addres(models.Model):
    street = models.CharField(verbose_name="Улица", max_length=150)
    suite = models.CharField(max_length=500)
    city = models.CharField(verbose_name="Город", max_length=100)
    zipcode = models.CharField(verbose_name="Индекс", max_length=50)
    lat = models.CharField(verbose_name="Широта", max_length=40)
    lng = models.CharField(verbose_name="Долгота", max_length=40)

    class Meta:
        verbose_name = "Адрес"
        verbose_name_plural = "Адреса"

    @property
    def full_address(self):
        return f"г. {self.city}, ул. {self.street}, д. {self.suite}, {self.zipcode}"        
    
    def __str__(self) -> str:
        return self.full_address

class Company(models.Model):
    name = models.CharField(verbose_name="Название", max_length=100)
    cathPhrase = models.CharField(verbose_name="Слоган", max_length=500)
    bs = models.CharField(max_length=500)

    def __str__(self) -> str:
        return self.name
        
    class Meta:
        verbose_name = "Компания"
        verbose_name_plural = "Компании"

class Person(models.Model):
    name = models.CharField(verbose_name="ФИО", max_length=200)
    username = models.CharField(verbose_name="Логин", max_length=30, unique=True)
    email = models.CharField(verbose_name="Email", max_length=40, unique=True)
    addres = models.ForeignKey(Addres, null=True, blank=True,
                               on_delete=models.SET_NULL, related_name="persons")
    phone = models.CharField(verbose_name="Телефон", max_length=50)
    website = models.CharField(verbose_name="Сайт", max_length=100)
    company = models.ForeignKey(Company, null=True, blank=True,
                                on_delete=models.SET_NULL, related_name="persons")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Персона"
        verbose_name_plural = "Персоны"
