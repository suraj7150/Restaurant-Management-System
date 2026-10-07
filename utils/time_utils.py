from utils import file_handling
from datetime import datetime, timedelta

class TimeManager:

    def get_current_time(self):
        return datetime.now()

    def calculate_booking_end(self, booking_start, booking_duration):

        start_time = datetime.strptime(
            booking_start,
            "%Y-%m-%d %H:%M:%S"
        )
        end_time = start_time + timedelta(
            hours= booking_duration
        )

        return end_time

    def is_booking_expired(self, booking_end):
        current_time = self.get_current_time()

        return current_time >= booking_end


    def update_expired_bookings(self):

        data = file_handling.read_data(
            "database/bookings.json"
        )

        table_data = file_handling.read_data(
            "database/tables.json"
        )
        for booking in data:
            if booking["status"] != "Active":
                continue

            booking_end = self.calculate_booking_end(
                booking["booking_start"],
                booking["booking_duration"]
            )
            if self.is_booking_expired(booking_end):
                booking["status"] = "Completed"

                for table in table_data:
                    if table["id"] in booking["table_ids"]:
                        table["status"] = "Available"
                        table["booking_start"] = None
                        table["booking_duration"] = None

        file_handling.write_data(
            "database/bookings.json",
            data
        )

        file_handling.write_data(
            "database/tables.json",
            table_data
        )
