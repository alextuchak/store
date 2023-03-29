from orders.forms import OrderForm
from django.views.generic.edit import CreateView


class OrderCreateView(CreateView):
    template_name = 'orders/order-create.html'
    form_class = OrderForm
