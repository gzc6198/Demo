#-*-coding:utf-8-*-
from django.core.cache import cache
def page_cache(views_func):
    def wrap(request,*args,**kwargs):
        key = 'Response-%s'% request.get_full_path()
        response = cache.get(key)
        if response==None:
            response = views_func(request)
            cache.set(key,response,3)
        return response
    return wrap