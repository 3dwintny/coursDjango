
from django.http import HttpResponse

#Utilidades 
from datetime import datetime 
import json 

def hello_word(request):
    now = datetime.now()
    return HttpResponse('Oh, hi, Current servver time is {now}'.format(now=str(now)))
def sorted_list(request):
    if request.method == "GET":
        numbers = [int (i) for i in request.GET['numbers'].split(',')]
        sorde_ints = sorted(numbers)
        data = {
            'status': 'ok',
            'numbers' : sorde_ints,
            'message': 'Integers sorde successfully.'
        }
    return HttpResponse(json.dumps(data, indent=4), content_type='application/json')

def say_hi(request, name, age):
    if request.method == "GET":
        if (age < 14):
            message = ('Sorry {}, you are not allowed here'.format(name))
        else:
            message = ('Hello {}, welcome to Ciangram'.format(name))
    
    return  HttpResponse(message)