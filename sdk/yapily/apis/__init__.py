
# flake8: noqa

# Import all APIs into this package.
# If you have many APIs here with many many models used in each API this may
# raise a `RecursionError`.
# In order to avoid this, import only the API that you directly need like:
#
#   from .api.application_api import ApplicationApi
#
# or import this package, but before doing it, use:
#
#   import sys
#   sys.setrecursionlimit(n)

# Import APIs into API package:
from yapily.api.application_api import ApplicationApi
from yapily.api.authorisations_api import AuthorisationsApi
from yapily.api.consents_api import ConsentsApi
from yapily.api.financial_data_api import FinancialDataApi
from yapily.api.financial_profile_api import FinancialProfileApi
from yapily.api.institutions_api import InstitutionsApi
from yapily.api.notifications_api import NotificationsApi
from yapily.api.payments_api import PaymentsApi
from yapily.api.users_api import UsersApi
from yapily.api.variable_recurring_payments_api import VariableRecurringPaymentsApi
from yapily.api.virtual_accounts_api import VirtualAccountsApi
