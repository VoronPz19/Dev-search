from .models import Project, Tag
from django.db.models import Q


def search_project(request):
    search_query = ''
    if request.GET.get('search_query'):
        search_query = request.GET.get('search_query')

    tag = Tag.objects.filter(name__exact=search_query)
    projects = Project.objects.distinct().filter(Q(title__icontains=search_query) |
                                                 Q(tag__in=tag))
    return projects, search_query
