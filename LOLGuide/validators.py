import re
from django.core.exceptions import ValidationError  # type: ignore
from django.utils.translation import gettext as _  # type: ignore

class ComplexPasswordValidator:
    def validate(self, password, user=None):
        if not re.search(r'[A-Z]', password):
            raise ValidationError(
                _("Пароль должен содержать хотя бы одну заглавную букву"),
                code='password_no_upper',
            )
        if not re.search(r'\d', password):
            raise ValidationError(
                _("Пароль должен содержать хотя бы одну цифру"),
                code='password_no_number',
            )
        if not re.search(r'[()\[\]{}|\\`~!@#$%^&*_\-+=;:\'",<>./?]', password):
            raise ValidationError(
                _("Пароль должен содержать хотя бы один специальный символ"),
                code='password_no_symbol',
            )
        
    def get_help_text(self):
        return _(
            "Ваш пароль должен содержать минимум 6 символов, заглавную букву, цифру и специальный символ."
        )
    
