import pandas as pd


df = pd.read_csv('hotels.csv', dtype={'id':str})

class Hotel:
    def __init__(self, id):
        self.id = id

    def Available(self):
        """Check if the hotel is available"""
        free = df.loc[df['id']==self.id, 'available'].squeeze()
        if free == 'yes':
            return True

    def book(self):
        """Book the hotel and change availability to no"""
        df.loc[df['id'] == id, 'available'] = 'no'
        df.to_csv('hotels.csv', index=False)

class ReservationTicket:
    def __init__(self, customer_name, hotel_obj):
        pass

    def generate(self):
        #content = return f"Name "
        pass

print(df)
id = input("Enter name of the hotel to book: ")

hotel = Hotel(id)
if hotel.Available:
    hotel.book()
    name = input("Enter your name: ")
    reservation_ticket = ReservationTicket(name, hotel)
    print(reservation_ticket.generate())
else:
    print("Hotel is booked out.")