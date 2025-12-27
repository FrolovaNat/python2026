def summarize_orders(*orders, **kwargs):
    if not orders:
        raise ValueError("Нет заказов для обработки")
currency = kwargs.get("currency", "RUB")
round_to = kwargs.get("round_to", 2)
total_items = 0
orders_count = len(orders)
avg_items = round(total_items/orders_count, round_to)
    return {
        "orders": orders_count,
        "total_items": total_items,
        "avg_items": avg_items,
        "currency": currency
        }

print(summarize_orders(("кофе", 2), ("чай", 1)))
print(summarize_orders(("пицца", 3), ("салат", 1), round_to=1, currency="USD"))
print(summarize_orders())

    #на слове return код не работает, не пойму в чем проблема
