

file = open("customer-orders.txt")
melon_cost = 1.00

def underpaid_cust(file):
    
    for line in file:
        line = line.rstrip()    #remove extra whitespace to the right
        words = line.split('|')    #use bar as the delimiter to split line into words

        customer_name = words[1]
        customer_melons = words[2]    
        customer_paid = float(words[3])
        

        customer_expected = float(customer_melons) * float(melon_cost)   #get expected paid amount for customer
        customer_expected = float(customer_expected)
        

        print(f"{customer_name} paid ${customer_paid:.2f}, expected ${customer_expected:.2f}")
        
        if customer_expected > customer_paid:
            print(f"{customer_name} has underpaid for their melons.")
        elif customer_expected < customer_paid:
            print(f"{customer_name} has overpaid for their melons.")
        print()

    file.close()

underpaid_cust(file)