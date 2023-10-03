from rest_framework.exceptions import ValidationError


class EstimatedTimeValidator:

    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val <= 120:
            return True
        else:
            raise ValidationError('Estimated time must be equal or less than 120 sec')


class PeriodicityValidator:
    def __init__(self, field):
        self.field = field

    def __call__(self, value):
        tmp_val = dict(value).get(self.field)
        if tmp_val < 7:
            return True
        else:
            raise ValidationError('Periodicity must not be less often than once in 7')
