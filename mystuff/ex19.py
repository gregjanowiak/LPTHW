def cheese_and_crackers(cheese_count,boxes_of_crackers):
    print(f"you have {cheese_count} cheeses")
    print(f"you have {boxes_of_crackers} boxes of crackers")

print("we can just give the function numbers directly")
cheese_and_crackers(20,30)

print("or, we can use variable from our script")
amount_of_cheese = 10
amount_of_crackers = 50
cheese_and_crackers(amount_of_cheese,amount_of_crackers)

print("we can do math inside too")
cheese_and_crackers(10 + 20, 5 + 6)
