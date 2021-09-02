from post.models import Person, Addres, Company
from django.contrib import admin


@admin.register(Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(Addres)
class AdressAdmin(admin.ModelAdmin):
    pass


@admin.register(Company)
class CompanyAdmin(admin.ModelAdmin):
    pass
