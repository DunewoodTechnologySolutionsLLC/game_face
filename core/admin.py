from django.contrib import admin
from core import models as core_models
from django.contrib.admin import AdminSite


@admin.register(core_models.Country)
class CountryAdmin(admin.ModelAdmin):
    pass


@admin.register(core_models.StateProvince)
class StateProvinceAdmin(admin.ModelAdmin):
    pass


@admin.register(core_models.Address)
class AddressAdmin(admin.ModelAdmin):
    pass


@admin.register(core_models.PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    pass


@admin.register(core_models.EmailAddress)
class EmailAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(core_models.Person)
class PersonAdmin(admin.ModelAdmin):
    pass


@admin.register(core_models.PersonEmailAddress)
class PersonEmailAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(core_models.PersonAddress)
class PersonAddressAdmin(admin.ModelAdmin):
    pass


@admin.register(core_models.PersonPhoneNumber)
class PersonPhoneNumberAdmin(admin.ModelAdmin):
    pass