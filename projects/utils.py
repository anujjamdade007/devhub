from .models import Project , Tag
from django.db.models import Q
from users.models import Profile


def searchproject(request):
    search_projects = ''

    if request.GET.get('search_projects'):
        search_projects = request.GET.get('search_projects')

    tags = Tag.objects.filter(name__icontains = search_projects)
     
    
    project = Project.objects.distinct().filter(Q(title__icontains = search_projects) |
                                                Q(description__icontains = search_projects) |
                                                Q(owner__name__icontains = search_projects) |
                                                Q(tags__in = tags))
    
    return project , search_projects
    