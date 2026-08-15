
"""
# Base GST Calculation

def calculate_price(base_price,tax_rate):
    return base_price * (1 + tax_rate)

print(calculate_price(1000,0.18))
print(calculate_price(500,0.18))

"""


from functools import partial
# Step 1: Define the Original Function
def calculate_price(base_price, tax_rate):
    return base_price * (1 + tax_rate)

# Step 2: Create a Pertially Applied Function With GST Fixed
price_with_gst = partial(calculate_price, tax_rate=0.18)

# Step 3: Now Use it Without Passing tax_rate Again
print(price_with_gst(1000))
print(price_with_gst(500))
