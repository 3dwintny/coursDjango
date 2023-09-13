from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.
posts = [
    {
        'title':'MontBlank',
        'user':{
            'name':'Edwin Tony Mejia',
            'picture':'https://picsum.photos/200'
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo':'https://picsum.photos/200/300',
    },
    {
        'title':'Via Lactea',
        'user':{
            'name':'Vidalia Merari Macario',
            'picture':'https://picsum.photos/200'
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo':'https://picsum.photos/seed/picsum/200/300',
    },
    {
        'title':'Nuevo auditorio',
        'user':{
            'name':'Candido Brandon Mejia ',
            'picture':'https://picsum.photos/200'
        },
        'timestamp': datetime.now().strftime('%b %dth, %y - %H:%M hrs'),
        'photo':'https://picsum.photos/200/300.webp',
    }

]

def list_posts(request):
    return render(request, 'feed.html', {'posts': posts})