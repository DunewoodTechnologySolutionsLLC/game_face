from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.views.generic import ListView, View
from django.views.generic import TemplateView, CreateView

from core import models as core_models


class IndexView(View):
    template_name = 'core/base.html'


class CountryListView(ListView):
    model = core_models.Country
    template_name = 'core/country/_list.html'


class StateProvinceListView(ListView):
    model = core_models.StateProvince
    template_name = 'core/state_province/_list.html'


class AddressListView(ListView):
    model = core_models.Address
    template_name = 'core/address/_list.html'


class AddressCreateView(CreateView):
    template_name = 'core/address/create.html'
    model = core_models.Address
    fields = '__all__'

class StateProvinceCreateView(CreateView):
    template_name = 'core/state_province/create.html'
    model = core_models.StateProvince
    fields = '__all__'

class CountryCreateView(CreateView):
    template_name = 'core/country/create.html'
    model = core_models.Country
    fields = '__all__'