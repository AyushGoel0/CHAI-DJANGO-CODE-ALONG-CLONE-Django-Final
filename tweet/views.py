from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def create(request):
    return render(request, 'create.html')

def delete(request, tweet_id):
    return render(request, 'delete.html', {'tweet_id': tweet_id})

def like(request, tweet_id):
    return render(request, 'like.html', {'tweet_id': tweet_id})
