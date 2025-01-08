products=[
    {"name":"Laptop","price":1000},
    {"name":"Mobile","price":500},
    {"name":"Tablet","price":300}
]
affordable_products={i["name"]: i["price"] for i in products if i["price"] < 500}
print(affordable_products)