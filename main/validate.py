from django.core.exceptions import ValidationError
import os

def validate_SVG_PNG(file):
    end = os.path.splitext(file.name)[1]
    if not end.lower() == '.png' and not end.lower() == '.svg':
        raise ValidationError('Загрузите изображение в формате PNG или SVG.')
