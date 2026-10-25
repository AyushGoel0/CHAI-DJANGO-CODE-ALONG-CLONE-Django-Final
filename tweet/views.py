from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'tweet/index.html')

def create(request):
    return render(request, 'tweet/create.html')

def delete(request, tweet_id):
    return render(request, 'tweet/delete.html', {'tweet_id': tweet_id})

def like(request, tweet_id):
    return render(request, 'tweet/like.html', {'tweet_id': tweet_id})