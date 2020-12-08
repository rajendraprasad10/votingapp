from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Like, add_Candidates
# Create your views here.
# index page creation
@login_required(login_url ='login')
def index(request):
    # get data from like model
    vote = Like.objects.all()
    user = request.user
    context = {
        'vote' : vote,
        'user' : user
    }
# add like condidates from view
    user = request.user
    if request.method == 'POST':
        like_id = request.POST.get('like_id')
        like_obj = add_Candidates.objects.get(id=like_id)

        if user in like_obj.liked.all():
            like_obj.objects.liked.remove(user)
        else:
            like_obj.liked.add(user)

    return render(request, 'index.html', context)