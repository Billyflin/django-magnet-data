# django
from django.utils.translation import gettext_lazy as _


class CurrencyAcronyms:
    CLF = "CLF"
    USD = "USD"
    EUR = "EUR"
    CLP = "CLP"
    UTM = "UTM"

    django_model_choices = (
        (CLP, _("CLP")),
        (CLF, _("CLF")),
        (USD, _("USD")),
        (EUR, _("EUR")),
        (UTM, _("UTM")),
    )


# currencies that have a single value for each month
MONTHLY_CURRENCIES = (CurrencyAcronyms.UTM,)
