class Table:
    def __init__(self):
        self.id = None
        self.size = None
        self.status = None
        self.__booking_start = None
        self.__booking_duration = None

    def get_booking_start(self):
        return self.__booking_start

    def set_booking_start(self, booking_start):
        self.__booking_start = booking_start

    def get_booking_duration(self):
        return self.__booking_duration 

    def set_booking_duration(self, booking_duration):
        self.__booking_duration = booking_duration
        
    def table_object(self):
        return {
            "id": self.id,
            "size": self.size,
            "status": self.status,
            "booking_start": self.__booking_start,
            "booking_duration": self.__booking_duration
        }

