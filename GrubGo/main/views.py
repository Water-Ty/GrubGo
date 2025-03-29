from django.views.generic import TemplateView

# Create your views here.


class TestView(TemplateView):
    template_name = "main/test.html"