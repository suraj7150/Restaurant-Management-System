from utils import staff_utils
from utils import file_handling
class AddStaff:

    def __init__(self):
        self.id = None
        self.name = None
        self.email = None
        self.password = None
        self.phone = None

    def add_staff(self):
        self.name = staff_utils.get_name()

        self.email = staff_utils.get_email()

        self.password = staff_utils.get_password()

        self.phone = staff_utils.get_phone()

        data = file_handling.read_data("database/user.json")

        for staff in data["staff"]:

            if staff["email"].lower() == self.email.lower():
                print("\t Staff with this email already exists...!")
                return

        if data["staff"]:
            self.id = max(staff["id"] for staff in data["staff"]) + 1
        else:
            self.id = 1

        new_staff = {
            "id": self.id,
            "name": self.name,
            "email": self.email,
            "password": self.password,
            "phone": self.phone
        }

        data["staff"].append(new_staff)

        file_handling.write_data(
            "database/user.json",
            data
        )
        print("‗" * 55)
        print("\t New Staff Add Successfully...")
        print(f"\t Staff : {self.name}")
        print("‗" * 55)


        
    