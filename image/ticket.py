import random

print("\n\nBus Ticket Booking System\n")
restart = 'Y'

ticket_data = []  # Store ticket and PNR information

while restart not in ('N', 'NO', 'n', 'no'):
    print("1. Check PNR status")
    print("2. Ticket Reservation")
    option = int(input("\nEnter your option: "))

    if option == 1:
        pnr_to_check = input("Enter your PNR to check: ")
        for ticket, pnr in ticket_data:
            if pnr == pnr_to_check:
                print(f"PNR status for {pnr}: Ticket {ticket}")
                break
        else:
            print("PNR not found.")
        exit(0)

    elif option == 2:
        people = int(input("\nEnter the number of tickets you want: "))
        for p in range(people):
            name = str(input("\nName: "))
            age = int(input("Age: "))
            gender = str(input("Male or Female: "))

            # Generate a random 6-digit PNR number
            pnr = str(random.randint(100000, 999999))

            ticket_data.append((p + 1, pnr))  # Store the ticket and PNR information

            print(f"Ticket: {p + 1}")
            print("Name: ", name)
            print("Age: ", age)
            print("Gender: ", gender)
            print(f"PNR: {pnr}")

        restart = input("\nDid you forget someone? (y/n): ")
        if restart in ('y', 'YES', 'yes', 'Yes'):
            restart = 'Y'
        else:
            print("\nTotal Tickets: ", people)
            for ticket, pnr in ticket_data:
                print(f"Ticket {ticket}: PNR {pnr}")
