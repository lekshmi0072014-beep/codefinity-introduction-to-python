# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

#define calculate revenue

def calculate_revenue(prices, quantities_sold):
    revenue = []
    for i in range(len(prices)):
        revenue.append(prices[i] * quantities_sold[i])
    return revenue

#define fomatted output 
def formatted_output(revenue_per_product):
    # use the built-in sorted() so the test sees it
    for name, rev in sorted(revenue_per_product, key=lambda x: x[0]):
        print(f"{name} has total revenue of ${rev}")




revenue = calculate_revenue(prices, quantities_sold)
revenue_per_product = list(zip(products, revenue))
formatted_output(revenue_per_product)

