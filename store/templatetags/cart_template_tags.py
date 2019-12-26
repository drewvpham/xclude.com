from django import template
from store.models import Order

register = template.Library()


@register.filter
def cart_item_count(user):
    if user.is_authenticated:
        total = 0
        qs = Order.objects.filter(user=user, ordered=False)
        if qs.exists():
            order_items = qs[0].items.all()
            for item in order_items:
                total+= item.quantity
            return total
    return total
