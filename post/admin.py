from post.models import Person, Addres, Company, Post
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

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    pass