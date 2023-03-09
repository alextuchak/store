from products.models import Basket
from django.core.cache import cache


def baskets(request):
    user = request.user
    cache_baskets = cache.get(user.username + '_baskets')
    if not cache_baskets:
        user_baskets = Basket.objects.filter(user=user)
        cache_baskets = cache.set(user.username + '_baskets', user_baskets, 600)
        cache_baskets = user_baskets
    return {'baskets': cache_baskets if user.is_authenticated else []}
