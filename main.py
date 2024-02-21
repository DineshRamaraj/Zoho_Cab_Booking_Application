# ... (previous code)


class Cab:
    taxicount = 0
    def __init__(self):
        Cab.taxicount += 1
        self.booked = False
        self.currentSpot = 'A'
        self.freeTime = 6
        self.totalEarnings = 0
        self.trips = []
        self.taxicount = Cab.taxicount
        self.id = self.taxicount
        self.amount = 0
        
    def setDetails(self, booked, currentSpot, freeTime, totalEarnings, tripDetails):
        self.booked = booked
        self.currentSpot = currentSpot
        self.freeTime = freeTime
        self.totalEarnings = totalEarnings
        self.trips.append(tripDetails)
        
    def printDetails(self):
        print("Taxi - ", self.id , " Total Earnings - " , self.totalEarnings)
        print("BookingID    CustomerID    From    To    PickupTime    DropTime    Amount")
        for trip in self.trips:
            # print(trip)
            print(trip[0],"               ", trip[1],"        ", trip[2], "    ", trip[3], "     ",trip[4], "           ", int(trip[5]), "      ", trip[6])
        print("--------------------------------------------------------------------------------------");
        
    
    def printTaxiDetails(self):
        print("Taxi - ", self.id , " Total Earnings - " , self.totalEarnings , " Current spot - " , self.currentSpot ," Free Time - " , int(self.freeTime))
        
        

def bookTaxi(customerID, pickupPoint, dropPoint, pickupTime, free_taxis_list):
    distanceBetweenpickUpandDrop = 0
    earning = 0
    nextfreeTime = 0
    nextSpot = 'Z'
    bookedTaxi = None
    tripDetail = ""

    for t in free_taxis_list:
        distanceBetweenCustomerAndTaxi = abs(ord(t.currentSpot) - ord(pickupPoint)) * 15
        bookedTaxi = t
        distanceBetweenpickUpandDrop = abs(ord(dropPoint) - ord(pickupPoint)) * 15
        earning = (distanceBetweenpickUpandDrop - 5) * 10 + 100

        dropTime = pickupTime + distanceBetweenpickUpandDrop / 15

        nextfreeTime = dropTime
        nextSpot = dropPoint

        tripDetail = (
            customerID,
            customerID,
            pickupPoint,
            dropPoint,
            pickupTime,
            dropTime,
            earning,
        )

        bookedTaxi.setDetails(
            True, nextSpot, nextfreeTime, bookedTaxi.totalEarnings + earning, tripDetail
        )
        print("Taxi ", bookedTaxi.id, " booked")
        return

def createTaxis(number):
    new_taxis = []
    for i in range(1, number+ 1):
        new_taxis.append(Cab())
        # print(Cab().id)
    
    return new_taxis
    
def getFreeTaxis(taxis, pickupTime, pickupPoint):
    new_free_taxis = [];
    for t in taxis:
        if(t.freeTime <= pickupTime and (abs(ord(t.currentSpot) - ord(pickupPoint)) <= pickupTime - t.freeTime)):
            new_free_taxis.append(t)
    return new_free_taxis

def main():
    taxis = createTaxis(4)

    while True:
        print("Call taxi booking")
        print("1. Cab Booking \n2. Cab Details\n3. exit")
        checking_number = input("Enter your Choices: ")

        if checking_number == "1":
            pickupPoint = input("Enter Pickup point: ")
            dropPoint = input("Enter Drop point: ")
            pickupTime = int(input("Enter Pickup time: "))

            if not ('A' <= pickupPoint <= 'F' and 'A' <= dropPoint <= 'F' and pickupPoint != dropPoint):
                print("Valid pickup and drop are A, B, C, D, E, F. Exiting")
                return

            free_taxis_list = getFreeTaxis(taxis, pickupTime, pickupPoint)

            if not free_taxis_list:
                print("No Taxi can be allotted. Exiting..")
                return

            free_taxis_list = sorted(free_taxis_list, key=lambda x: x.totalEarnings)

            bookTaxi(1, pickupPoint, dropPoint, pickupTime, free_taxis_list)

        elif checking_number == "2":
            for t in taxis:
                t.printDetails()
            for t in taxis:
                t.printTaxiDetails()
        elif checking_number == "3":
            print("Thank you Sir...")
            exit()
        else:
            print("Please Enter a Valid Number")


if __name__ == "__main__":
    main()
