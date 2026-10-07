from auth.login import Login
from utils.time_utils import TimeManager

TimeManager().update_expired_bookings()

Login().login_menu()
