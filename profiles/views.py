from django.shortcuts import render
from .models import Profile


# Sed placerat quam in pulvinar commodo. Nullam laoreet consectetur ex, sed consequat libero pulvinar eget. Fusc
# faucibus, urna quis auctor pharetra, massa dolor cursus neque, quis dictum lacus d
def index(request):
    """
    Here is the profiles list view and what it renders below

    Returns:
        | Profiles list based on users' username
        | that way they can be differentiated
        | Then this is called in oc_lettings_site/urls.py

    """
    profiles_list = Profile.objects.all()
    context = {'profiles_list': profiles_list}
    return render(request, 'profiles/index.html', context)


# Aliquam sed metus eget nisi tincidunt ornare accumsan eget lac laoreet neque quis, pellentesque dui. Nullam
# facilisis pharetra vulputate. Sed tincidunt, dolor id facilisis fringilla, eros leo tristique lacus,
# it. Nam aliquam dignissim congue. Pellentesque habitant morbi tristique senectus et netus et males
def profile(request, username):
    """
    Here is the profile view and what it renders below

    Returns:
        | Let's suppose we clicked on a username in the profiles list
        | Now we can access to the parameters that are associated
        | Then this is called in oc_lettings_site/urls.py

    """
    profile = Profile.objects.get(user__username=username)
    context = {'profile': profile}
    return render(request, 'profiles/profile.html', context)
