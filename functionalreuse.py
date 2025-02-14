"""
FUNCTIONAL REUSABILITY
You are building an e-commerce order processing system, and you need to calculate discounts, taxes, and final prices for multiple products. I nstead of writi
"""

price = int(input("Enter price:"))
discount = int(input("Enter discount percentage"))
#function to give discount
def apply_discount(p, d):
    discount_price = (p * d/100)
    return p - discount_price
#print(apply_discount(price,discount))
#function to  calculate tax after discount application
def calculate_taxes(price):
    vattax = 16
    result = price * (vattax / 100)
    return result
#THIS FUNCTION WILL THEN GET OUR FINAL PRICE
def get_final_price(price,discount,vattax):
    discountedPrice =apply_discount(price,discount)
    tax = calculate_taxes(discountedPrice)
    result_price= discountedPrice + tax
    return (f"The item discount price {discountedPrice} it has a tax" f"of {tax} so the final price is {result_price}")

 print(get_final_price(price,discount))