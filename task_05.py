# обработка заказов на складе

from pymonad.tools import curry
from pymonad.state import State

warehouse_init = {
    'orders': [],
    'stock': {
        'apples': 50,
        'milk': 30,
        'bread': 40
    }
}

warehouse_state = State.insert(warehouse_init['orders'])


@curry(3)
def process_order(product, amount, orders_done):
    def stock_computation(stock):
        new_stock = stock.copy()
        new_stock[product] -= amount
        return orders_done + [f"{product}:{amount}"], new_stock
    return State(stock_computation)

plan = (
    warehouse_state
    .then(process_order('apples', 10))
    .then(process_order('milk', 5))
    .then(process_order('bread', 8))
)

result = plan.run(warehouse_init['stock'])
print(result)