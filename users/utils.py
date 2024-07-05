from .models import Profile , Skills
from django.db.models import Q


def searchuser(request):
    search_user = ''

    if request.GET.get('search_user'):
        search_user = request.GET.get('search_user')

    skills = Skills.objects.filter(name__icontains = search_user)
    
    profile = Profile.objects.distinct().filter(Q(name__icontains = search_user) | 
                                     Q(headline__icontains = search_user) |
                                     Q(skills__in = skills) )
    
    return search_user , profile
    