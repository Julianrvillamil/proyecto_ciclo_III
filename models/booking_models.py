from pydantic import BaseModel
from datetime import datetime

##ITS NOT THE TABLE, ITS A WAY TO CATCH THE INFORMATION
##WHAT WE ARE DOING IS LIKE AN ABSTRACTION OF THE MODEL IN THE TABLES OF THE DB
##ALSO WE ONLY BRING SOME THINGS, LIKE IN A SELECT QUERY, IN THIS CASE FOR THE INPUT  AND THE OUTPUT 
class BookingIn(BaseModel):
    username: str
    typeroom: str
    departure_date: datetime
    arrival_date: datetime
    
class BookingOut(BaseModel):
    id_booking: int
    username: str
    departure_date: datetime
    arrival_date: datetime
    typeroom: str
    value: int