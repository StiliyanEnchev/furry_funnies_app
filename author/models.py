from django.core.validators import MinLengthValidator
from django.db import models

from author.validators import only_letters_validator, six_digits_validator, is_digits_validator


# Create your models here.
class Author(models.Model):
    first_name = models.CharField(
        max_length=40,
        validators=[
            MinLengthValidator(4),
            only_letters_validator,
        ]
    )

    last_name = models.CharField(
        max_length=50,
        validators=[
            MinLengthValidator(2),
            only_letters_validator,
        ]
    )

    passcode = models. CharField(
        help_text="Your passcode must be a combination of 6 digits",
        validators=[
            six_digits_validator,
            is_digits_validator
        ]
    )

    pets_number = models.PositiveSmallIntegerField()

    info = models.TextField(
        blank=True,
        null=True,
    )

    image_url = models.URLField(
        blank=True,
        null=True,
    )