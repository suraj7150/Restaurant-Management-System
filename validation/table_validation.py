def validate_id(table_id):
    try:
        table_id = int(table_id)
    except (ValueError, TypeError):
        return False

    return table_id > 0

def validate_size(size):
    try:
        size = int(size)

        all_size = [2,4,6,8]

        size in all_size

    except (ValueError, TypeError):
        return False

    return size in all_size

def validate_booking_duration(booking_duration):
    try:
        booking_duration = int(booking_duration)

    except (ValueError, TypeError):
        return False

    return 1<= booking_duration <=24

def validate_customer_count(customer_count):
    try:
        customer_count = int(customer_count)
    except (ValueError, TypeError):
        return False

    return  customer_count > 0
