import sys

meal_cost = float(input())

tip_percentage = int(input())

sales_tax = int(input())

total_cost = meal_cost + (meal_cost*(tip_percentage/100)+(meal_cost*(sales_tax/100)))

print('The total meal cost is', round(total_cost), 'dollars.')