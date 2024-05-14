from django.http import JsonResponse, HttpResponseNotFound
from ser.models import Category, Quote
import json, random, datetime

def categories(request):
    categories = Category.objects.all()
    return JsonResponse([{'name': str(c).lower(), 'id': c.id} for c in categories], safe=False, json_dumps_params={'ensure_ascii': False})

def prepare_quote(quote):
    res = {
        'id': quote.id,
        'quote': quote.text,
        'author': quote.author,
        'categoryId': quote.category.id
    }
    return res


def prepate_ban_ids(banIds):
    banIds = banIds.split(',') if banIds else []
    banIds = [int(b) for b in banIds]
    return banIds

def quotes(request):
    banIds = prepate_ban_ids(request.GET.get('ban'))
    quotesCount = Quote.objects.all().count()
    picked = random.randint(2, quotesCount-2)
    while picked in banIds:
        picked = random.randint(2, quotesCount-2)
    quote = Quote.objects.get(pk=picked)
    res = prepare_quote(quote)
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})

def quotes_by_category(request, categoryId):
    banIds = prepate_ban_ids(request.GET.get('ban'))
    category=Category.objects.get(pk=categoryId)
    quotesOfCategory = Quote.objects.filter(category=category)
    quotesOfCategoryIds = [q.id for q in quotesOfCategory]
    allowedIds = set(quotesOfCategoryIds).difference(banIds)
    if len(allowedIds) == 0:
        return HttpResponseNotFound()
    
    quote = Quote.objects.get(pk = random.choice(list(allowedIds)))
    res = prepare_quote(quote)
    return JsonResponse(res, safe=False, json_dumps_params={'ensure_ascii': False})


daily_quote = {
    'quone': None,
    'day': None
}

def quotes_daily(request):
    now = datetime.date.today()
    if daily_quote['day'] is None or now > daily_quote['day']:
        daily_quote['quone'] = quotes(request)
        daily_quote['day'] = now
    return daily_quote['quone']