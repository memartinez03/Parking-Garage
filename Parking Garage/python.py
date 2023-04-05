class ParkingGarage:
    def __init__(self, num_tickets, num_parking_spaces):
        self.tickets = [i for i in range(1, num_tickets + 1)]
        self.parking_spaces = [i for i in range(1, num_parking_spaces + 1)]
        self.current_ticket = {}

    def take_ticket(self):
        if self.tickets:
            ticket = self.tickets.pop(0)
            self.parking_spaces.pop(0)
            self.current_ticket[ticket] = {"paid": False}
            print(f"Your ticket number is {ticket}")
        else:
            print("Sorry, the garage is full.")

    def pay_for_parking(self):
        ticket = int(input("Enter your ticket number: "))
        if self.current_ticket.get(ticket):
            if not self.current_ticket[ticket]["paid"]:
                payment = input("Please enter payment amount: ")
                if payment:
                    self.current_ticket[ticket]["paid"] = True
                    print("Payment received. You have 15 minutes to leave.")
                else:
                    print("No payment received.")
            else:
                print("Ticket already paid.")
        else:
            print("Invalid ticket number.")

    def leave_garage(self):
        ticket = int(input("Enter your ticket number: "))
        if self.current_ticket.get(ticket):
            if self.current_ticket[ticket]["paid"]:
                print("Thank you, have a nice day!")
                self.parking_spaces.append(ticket)
                self.tickets.append(ticket)
                del self.current_ticket[ticket]
            else:
                print("Payment not received. Please pay before leaving.")
        else:
            print("Invalid ticket number.")

parking_garage = ParkingGarage(5, 5)

parking_garage.take_ticket()

parking_garage.pay_for_parking()

parking_garage.leave_garage()
