from django.shortcuts import render
from django.views.generic import TemplateView

def homePageView(request):

    context = {
        "inventoryList": ["Widget 1", "Widget 2", "Widget 3"],
        "greeting": "Thank you for visiting!"
    }

    return render(request, "home.html",context)

class AboutPageView(TemplateView):
    template_name = "about.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["contactAddress"] = "123 Main Street"
        context["phoneNumber"] = "(555)-555-555"
        return context