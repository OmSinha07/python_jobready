class train:
    def __init__(self,name,fare,seats):
        self.name=name
        self.fare=fare
        self.seats=seats
    def getStatus(self):
        print(f"The name of the train is {self.name}")
        print(f"The seats avauilable in the train are{self.seats}")
    def fareInfo(self):
        print(f"The price of the ticket is Rs {self.fare}")
    def bookTicket(self):
        if(self.seats>0):
            print(f"Your ticket has been booked!Your seat number is {self.seats}")
            self.seats=self.seats-1
        else:
         print("the train is full")

puribbsr=train("Puribbsr",150,100)
puribbsr.getStatus()
puribbsr.fareInfo()
puribbsr.bookTicket()
puribbsr.getStatus()