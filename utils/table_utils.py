from utils import file_handling

def get_available_tables():

    data = file_handling.read_data("database/tables.json")

    available_tables = []

    for table in data:
        if table.get("status") == "Available":
            available_tables.append(table)

    return available_tables


def is_multiple_tables(customer_count):

    available_tables = get_available_tables()

    if not available_tables:
        return False

    max_size_table = available_tables[0]["size"]

    for table in available_tables:
        if table["size"] > max_size_table:
            max_size_table = table["size"]

    if max_size_table < customer_count:
        return True
    else:
        return False
        

def get_one_table(customer_count):

    available_tables = get_available_tables()

    suitable_tables = []

    suitable_tables.append(available_tables[0])

    best_table = available_tables[0]

    for table in available_tables:
        if(
            table["size"] >= customer_count and
            best_table["size"]< table["size"]
        ):
            best_table = table
            break

    for table in available_tables:
        if(
            table["size"] >= customer_count and
            suitable_tables[-1]["size"]<= table["size"]
        ):
            suitable_tables.append(table)

    return best_table, suitable_tables

def get_multiple_tables(customer_count):

    available_tables = get_available_tables()

    selected_tables = []
    remaining_customers = customer_count

    while remaining_customers > 0:

        if not available_tables:
            return []

        largest_table = available_tables[0]

        for table in available_tables:

            # if largest_table == None:
            #     largest_table = table
            if table["size"] > largest_table["size"]:
                largest_table = table

        selected_tables.append(largest_table)

        remaining_customers -= largest_table["size"]

        available_tables.remove(largest_table)

    return selected_tables

def booking_object(self,booking_id, customer_name,
    customer_email, customer_phone, customer_count,
    table_ids, booking_start, booking_duration, status
):
    book_table = {
        "booking_id": booking_id,
        "customer_name": customer_name,
        "customer_email": customer_email,
        "customer_phone": customer_phone,
        "customer_count": customer_count,
        "table_ids": table_ids,
        "booking_start": booking_start,
        "booking_duration": booking_duration,
        "status": status
    }
    return book_table



    
    