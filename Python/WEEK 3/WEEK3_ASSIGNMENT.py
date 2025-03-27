def calculate_discount(price, discount_percent):
    """Calculate the final price after applying a discount if it's 20% or higher."""
    return price - (price * discount_percent / 100) if discount_percent >= 20 else price

# Get user input for the original price and discount percentage
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

# Print the final price after applying the discount (if applicable)
print(f"Final price: ${calculate_discount(price, discount_percent):.2f}")
