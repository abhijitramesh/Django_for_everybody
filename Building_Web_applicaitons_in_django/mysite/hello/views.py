from django.http import HttpResponse

# Create your views here.

def cookie(request):
    print(request.COOKIES)
    oldval = request.COOKIES.get('zap',None)
    resp = HttpResponse('In a view - the zap cookie value is '+ str(oldval))
    if oldval:
        resp.set_cookie('zap',int(oldval)+1)
    else:
        resp.set_cookie('zap',42)
    resp.set_cookie('sakaicar',42,max_age=1000)
    resp.set_cookie('dj43_cookie','08808cfb',max_age=1000)
    return resp


def sessfun(request):
    num_visits = request.session.get('num_visits',0)+1
    request.session['num_visits'] = num_visits
    if num_visits > 4 : del(request.session['num_visits'])
    resp = HttpResponse('view count='+str(num_visits))
    resp.set_cookie('dj43_cookie','08808cfb',max_age=1000)
    return resp