from django.views.generic import TemplateView

# Adicione esta classe
class HomeView(TemplateView):
    template_name = 'home/dashboard.html' # Vamos criar este template
