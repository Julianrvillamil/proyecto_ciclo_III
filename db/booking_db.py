from datetime import datetime#transaction#booking
from pydantic import BaseModel

##THE DEFINITION OF THE TABLES IN THE DATA BASE
class BookingInDB(BaseModel):
    id_booking: int
    username: str
    departure_date: datetime
    arrival_date: datetime
    typeroom: str
    value: int

database_bookings = []##HAVE A DB FOR bookingS
generator = {"id":0}##FOR THE AUTO INCREMENT IN THE ID

##FUNCTION THAT SAFE THE booking
def save_booking(booking_in_db: BookingInDB):
    generator["id"] = generator["id"] + 1 ##AUTO INCREMENT THE ID
    booking_in_db.id_booking = generator["id"]##DEFINE TO ENTER THE ID IN THE SAFE OF THE booking SAFE
    database_bookings.append(booking_in_db)##SAFE THE booking IN THE ""DB_bookingS"" ABOVE(line12)
    return booking_in_db