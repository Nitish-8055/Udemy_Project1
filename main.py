import pandas as pd


df = pd.read_csv('hotels.csv', dtype={'id':str})
df_cards = pd.read_csv('cards.csv').to_dict(orient='records')
df_cards_security = pd.read_csv('card_security.csv')

class Hotel:
    def __init__(self, id):
        self.id = id
        self.name = df.loc[df["id"] == self.id, 'name'].squeeze()

    def available(self):
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
        self.customer_name = customer_name
        self.hotel = hotel_obj

    def generate(self):
        content = f"""
        Thank you for your reservation!
        Here is your booking data:
            Name: {self.customer_name}
            Hotel name: {self.hotel.name}
        """
        return content


class CreditCard:
    def __init__(self, number):
        self.number = number

    def validate(self,expiration, holder, cvc):
        card_data = {'number': self.number, 'expiration': expiration,
                     'holder': holder, 'cvc': cvc}
        if card_data in df_cards:
            return True

class SecureCreditCard(CreditCard):
    def authenticate(self, given_password):
        password = df_cards_security.loc[df_cards_security['number']==self.number, 'password'].squeeze()
        if password == given_password:
            return True


class Spa():
    def __init__(self, name, id):
        self.name = name
        self.hotel_name = df.loc[df['id'] == id, 'name'].squeeze()

    def generate(self):
        return f"""
        Thank you for your Spa reservation!
        Here is your spa booking data:
            Name: {self.name}
            Hotel name: {self.hotel_name}
        """


print(df)
id = input("Enter name of the hotel to book: ")

hotel = Hotel(id)
if hotel.available():
    credit_card = SecureCreditCard(number=1234567890123456)
    if credit_card.validate(expiration='12/26', holder='JOHN SMITH', cvc=123):
        if credit_card.authenticate(given_password='mypass'):
            hotel.book()
            name = input("Enter your name: ")
            reservation_ticket = ReservationTicket(name, hotel)
            print(reservation_ticket.generate())

            choice = input("Do you want to book a spa package? ")
            spa = Spa(name, id)
            if choice == 'yes':
                print(spa.generate())
        else:
            print("Credit card authentication failed")
    else:
        print("There was a problem with your payment")
else:
    print("Hotel is booked out.")