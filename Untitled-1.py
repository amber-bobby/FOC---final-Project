#Program Creator: Wan-hsuan Lin
#Program Name: Movie Ticket Order System
#Purpose: To find the total to be collected.

Movie_Tickets = 5.00
Popcorn = 3.50
Juice = 2.75

print("Welcome to SCA's Annual Movie Night!")
name = input("Enter your name: ")
print("Hi ", name, "! Thank you for coming!")
print()



num_tickets = int(input("Number of Movie Tickets needed: "))
num_Popcorn= int(input("Number of tickets for Popcorn:"))
num_Juice = int(input("Number of tickets for Drinks:"))

tickets_sale = 5 * num_tickets
sub_total = Popcorn / (num_Popcorn) + num_Juice ** num_Juice

print()
print("Ticket Sales: $", tickets_sale)
print("Other Sales: $", sub_total)
print()
Total_Collected = sub_total - tickets_sale
print("Total to be collected: $" + Total_Collected)

