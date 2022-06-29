km=int(input("Bitte gib deine Kilometer ein: \n  "))

def total_expenses(km):
    start_price=4.80
    costs=1.70
    total_cost=costs*km+start_price
    return total_cost

costs=total_expenses(km)
print(costs)