class Guest:
    """Class to represent a hotel guest"""

    def __init__(self, guestID, name, email, phoneNumber, address):
        self.__guestID = guestID
        self.__name = name
        self.__email = email
        self.__phoneNumber = phoneNumber
        self.__address = address

    # Setter and Getter methods for Guest attributes
    def setGuestID(self, guestID):
        self.__guestID = guestID

    def getGuestID(self):
        return self.__guestID

    def setName(self, name):
        self.__name = name

    def getName(self):
        return self.__name

    def setEmail(self, email):
        self.__email = email

    def getEmail(self):
        return self.__email

    def setPhoneNumber(self, phoneNumber):
        self.__phoneNumber = phoneNumber

    def getPhoneNumber(self):
        return self.__phoneNumber

    def setAddress(self, address):
        self.__address = address

    def getAddress(self):
        return self.__address

    # Function to search for a reservation by the guest
    def searchReservation(self):
        """Search for a guest's reservation."""
        pass  # Functionality to search for reservations by guest ID

    # Function to modify a reservation
    def modifyReservation(self):
        """Modify a reservation made by the guest."""
        pass  # Modify reservation details for the guest

    # Function to cancel a reservation
    def cancelReservation(self):
        """Cancel the reservation made by the guest."""
        pass  # Cancel the guest's reservation


# Create a Guest object and print attributes
guest1 = Guest("M244", "Maitha Alteneiji", "maithaalteneiji244@example.com", "545-454-1", "AlMizhar 3")
print("Guest Info")
print("ID:", guest1.getGuestID())
print("Name:", guest1.getName())
print("Email:", guest1.getEmail())
print("Phone:", guest1.getPhoneNumber())
print("Address:", guest1.getAddress())


class Reservation:
    """Class to represent a hotel reservation"""

    def __init__(self, reservationID, checkInDate, checkOutDate, status, totalPrice):
        self.__reservationID = reservationID
        self.__checkInDate = checkInDate
        self.__checkOutDate = checkOutDate
        self.__status = status
        self.__totalPrice = totalPrice

    # Setter and Getter methods for Reservation attributes
    def setReservationID(self, reservationID):
        self.__reservationID = reservationID

    def getReservationID(self):
        return self.__reservationID

    def setCheckInDate(self, checkInDate):
        self.__checkInDate = checkInDate

    def getCheckInDate(self):
        return self.__checkInDate

    def setCheckOutDate(self, checkOutDate):
        self.__checkOutDate = checkOutDate

    def getCheckOutDate(self):
        return self.__checkOutDate

    def setStatus(self, status):
        self.__status = status

    def getStatus(self):
        return self.__status

    def setTotalPrice(self, totalPrice):
        self.__totalPrice = totalPrice

    def getTotalPrice(self):
        return self.__totalPrice

    # Function to modify the reservation details
    def modifyDetails(self):
        """Modify the reservation details (dates, room, etc.)."""
        pass  # Modify the reservation details such as check-in date, check-out date, etc.

    # Function to cancel the reservation
    def cancel(self):
        """Cancel the reservation."""
        pass  # Cancel the reservation and update its status

    # Function to calculate total charges for the reservation
    def calculateCharges(self):
        """Calculate the total charges for the reservation."""
        pass  # Calculate charges based on room rates and reservation duration


# Create a Reservation object and print attributes
reservation1 = Reservation("M206", "2024-12-08", "2024-12-10", "Confirmed", 600.00)
print("\nReservation Info")
print("ID:", reservation1.getReservationID())
print("Check-in Date:", reservation1.getCheckInDate())
print("Check-out Date:", reservation1.getCheckOutDate())
print("Status:", reservation1.getStatus())
print("Total Price:", reservation1.getTotalPrice())


class Room:
    """Class to represent a hotel room"""

    def __init__(self, roomID, roomType, pricePerNight, floorNumber, isAvailable):
        self.__roomID = roomID
        self.__roomType = roomType
        self.__pricePerNight = pricePerNight
        self.__floorNumber = floorNumber
        self.__isAvailable = isAvailable

    # Setter and Getter methods for Room attributes
    def setRoomID(self, roomID):
        self.__roomID = roomID

    def getRoomID(self):
        return self.__roomID

    def setRoomType(self, roomType):
        self.__roomType = roomType

    def getRoomType(self):
        return self.__roomType

    def setPricePerNight(self, pricePerNight):
        self.__pricePerNight = pricePerNight

    def getPricePerNight(self):
        return self.__pricePerNight

    def setFloorNumber(self, floorNumber):
        self.__floorNumber = floorNumber

    def getFloorNumber(self):
        return self.__floorNumber

    def setIsAvailable(self, isAvailable):
        self.__isAvailable = isAvailable

    def getIsAvailable(self):
        return self.__isAvailable

    # Function to check room availability
    def checkAvailability(self):
        """Check if the room is available."""
        pass  # Check if the room is available for booking

    # Function to get the price per night of the room
    def getPrice(self):
        """Return the price per night for the room."""
        return self.__pricePerNight


# Create a Room object and print attributes
room1 = Room("Room204", "Deluxe", 200.00, 2, True)
print("\nRoom Info")
print("ID:", room1.getRoomID())
print("Type:", room1.getRoomType())
print("Price per Night:", room1.getPricePerNight())
print("Floor Number:", room1.getFloorNumber())
print("Available:", room1.getIsAvailable())


class Payment:
    """Class to represent payment details for a reservation"""

    def __init__(self, paymentID, amount, paymentMethod, paymentDate, status):
        self.__paymentID = paymentID
        self.__amount = amount
        self.__paymentMethod = paymentMethod
        self.__paymentDate = paymentDate
        self.__status = status

    # Setter and Getter methods for Payment attributes
    def setPaymentID(self, paymentID):
        self.__paymentID = paymentID

    def getPaymentID(self):
        return self.__paymentID

    def setAmount(self, amount):
        self.__amount = amount

    def getAmount(self):
        return self.__amount

    def setPaymentMethod(self, paymentMethod):
        self.__paymentMethod = paymentMethod

    def getPaymentMethod(self):
        return self.__paymentMethod

    def setPaymentDate(self, paymentDate):
        self.__paymentDate = paymentDate

    def getPaymentDate(self):
        return self.__paymentDate

    def setStatus(self, status):
        self.__status = status

    def getStatus(self):
        return self.__status

    # Function to process payment
    def processPayment(self):
        """Process the payment for the reservation."""
        pass  # Code to process payment for the reservation

    # Function to refund payment
    def refund(self):
        """Refund the payment if the reservation is canceled."""
        pass  # Code to handle refunds if the reservation is canceled


# Create a Payment object and print attributes
payment1 = Payment("M4466", 600.00, "Credit Card", "2024-12-08", "Completed")
print("\nPayment Info")
print("ID:", payment1.getPaymentID())
print("Amount:", payment1.getAmount())
print("Method:", payment1.getPaymentMethod())
print("Date:", payment1.getPaymentDate())
print("Status:", payment1.getStatus())

