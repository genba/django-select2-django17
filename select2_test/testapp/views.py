from django.views.generic import FormView
from forms import TestForm

class Startpage(FormView):
    template_name = 'startpage.html'
    form_class = TestForm
