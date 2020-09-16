
from django.http import HttpResponse
#import responses as resp


# Create your views here.


def count(request) :
    #resp.set_cookie('dj4e_cookie', '1770ae9e', max_age=1000)
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    return HttpResponse('view count='+str(num_visits))

