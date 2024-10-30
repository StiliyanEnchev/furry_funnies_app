from django.core.exceptions import ValidationError


def only_letters_validator(value):
    if not value.isalpha():
        raise ValidationError(
            'Your name must contain letters only!'
        )


def six_digits_validator(value):
    if len(value) != 6:
        raise ValidationError(
            "Your passcode must be exactly 6 digits!"
        )


def is_digits_validator(value):
    if not value.isdigit():
        raise ValidationError(
            "Your passcode must be only digits!"
        )