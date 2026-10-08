from validation import user_validation
from utils import file_handling
class DeleteStaff:

    def __init__(self):
        self.staff_id = None

    def delete_staff(self):
        while True:

            self.staff_id = input("\t Enter Staff Id : ")

            if user_validation.validate_id(self.staff_id):
                self.staff_id = int(self.staff_id)
                break
            else:
                print("\t Invalid Staff Id...!")

        data = file_handling.read_data("database/user.json")

        for staff in data["staff"]:

            if staff["id"] == self.staff_id:
                data["staff"].remove(staff)

                file_handling.write_data(
                    "database/user.json",
                    data
                )
                print("\t Staff Removed Successfully!")
                return

        print("\t Staff Not found...!")
           


    
