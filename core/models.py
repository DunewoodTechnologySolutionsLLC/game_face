from django.db import models
from django.contrib.auth.models import User

from django.core.validators import MinLengthValidator, DecimalValidator


class Country(models.Model):
    name = models.TextField(max_length=40)

    def __str__(self):
        return self.name


class StateProvince(models.Model):
    country = models.ForeignKey(Country,
                                models.PROTECT, blank=False, null=False)
    name = models.CharField(max_length=20)
    abbreviation = models.CharField(max_length=4)

    def __str__(self):
        return self.abbreviation


class Address(models.Model):
    state_province = models.ForeignKey(StateProvince,
                                       models.SET_NULL, blank=False, null=True)
    line_one = models.CharField(max_length=40)
    line_two = models.CharField(max_length=40, blank=True, null=True)
    city = models.CharField(max_length=40)
    postal_code = models.PositiveIntegerField()
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.formatted_string()

    def formatted_string(self, single_line=False):
        if single_line:
            if self.line_two:
                return "{}, {}, {}, {} {}".format(self.line_one, self.line_two,
                                                  self.city, self.state_province.abbreviation, self.postal_code)
            return "{}, {}, {} {}".format(self.line_one, self.city, self.state_province.abbreviation, self.postal_code)
        if self.line_two:
            return "{}, {}, {}, \n {} {}".format(self.line_one, self.line_two,
                                                 self.city, self.state_province.abbreviation, self.postal_code)
        return "{}, {}, \n {} {}".format(self.line_one, self.city, self.state_province.abbreviation, self.postal_code)


class PhoneNumber(models.Model):
    number = models.CharField(max_length=10)
    is_mobile = models.BooleanField(default=False)
    type = models.CharField(max_length=20,
                            choices=(('FAX', 'Fax'), ('CELL', 'Cell'), ('HOME', 'Home'), ('BUSINESS', 'Business')))
    is_primary = models.BooleanField(default=False)

    def __str__(self):
        return self.number


class PhoneNumberExtension(models.Model):
    phone_number = models.ForeignKey(PhoneNumber, models.CASCADE)
    extension = models.PositiveIntegerField()


class EmailAddress(models.Model):
    address = models.EmailField()
    type = models.CharField(max_length=20,
                            choices=(('PERSONAL', 'Personal'), ('WORK', 'Work')))
    is_primary = models.BooleanField(default=False)


class Person(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return '{} {}'.format(self.first_name, self.last_name)

    def full_name(self):
        return self.__str__()


class PersonAddress(Address):
    person = models.OneToOneField(Person,
                                  models.CASCADE, blank=False, null=False)


class PersonEmailAddress(EmailAddress):
    person = models.OneToOneField(Person,
                                  models.CASCADE, blank=False, null=False)


class PersonPhoneNumber(PhoneNumber):
    person = models.OneToOneField(Person,
                                  models.CASCADE, blank=False, null=False)