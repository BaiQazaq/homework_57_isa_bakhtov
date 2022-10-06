from django.views.generic import TemplateView
from tracker_app.models import Task


class IndexView(TemplateView):
    template_name = 'index.html'
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['tasks'] = Task.objects.filter(is_deleted=False)
        return context