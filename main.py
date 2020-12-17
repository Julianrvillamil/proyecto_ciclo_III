##IMPORT OF OTHER FOLDERS
from db.user_db import UserInDB
from db.user_db import update_user, get_user

from db.booking_db import BookingInDB#booking#transaction#balance
from db.booking_db import save_booking

from models.user_models import UserIn, UserOut

from models.booking_models import BookingIn, BookingOut
###################################

##ALSO IMPORTANT IMPORTS
import datetime
from fastapi import FastAPI
from fastapi import HTTPException##FOR DISPLAY THE ERRORS, LIKE ERROR ""404 PAGE NOT FOUND""
####################################

api = FastAPI()##CREATE THE API-REST

from fastapi.middleware.cors import CORSMiddleware

origins = [
    "http://localhost.tiangolo.com", "https://localhost.tiangolo.com",
    "http://localhost", "http://localhost:8080",
]
api.add_middleware(
  CORSMiddleware, allow_origins=origins,
  allow_credentials=True, allow_methods=["*"], allow_headers=["*"],
)

##IN THIS CASE WE USE post THAT IS FOR CREATE BECAUSE WE ARE PASSING A PASSWORD
@api.post("/user/auth/")##TO ASOCIATE THE DEF BELOW TO A WEB SERVICE WE USE THIS DECORATOR @api.post/get/pot/delete
async def auth_user(user_in: UserIn):##async=asynchronous ## RESIVE THE USER
    user_in_db = get_user(user_in.username)## == THE RESPONSE OF THE METHOD THAT CONFIRMS THAT THE USER EXISTS IN users_db.py
    if user_in_db == None:##IF DOESNT EXIST THE USER NAME DISPLAY ERROR 404
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    if user_in_db.password != user_in.password:##IF THE PASSWOR DOESNT COINSIDE 
        return {"Autenticado": False}
    return {"Autenticado": True}

##get TO READ
@api.get("/user/count/{username}")#balance
async def get_count(username: str):##ALLWAYS WE USE get WE MUST HAVE TO USE IN THE PARAMETER OF THE DEF
    user_in_db = get_user(username)##VERYFI THAT USER EXIST
    if user_in_db == None:
        raise HTTPException(status_code=404,
                            detail="El usuario no existe")
    user_out = UserOut(**user_in_db.dict())##THE ** MAPING THE USER, THIS MEANS THEY ONLY GIVE THE PARAMETERS THAT ARE IN USER_MODELS.PY
    return user_out

##put TO CHANGE
##@api.put("/user/booking/")#booking#transaction
##async def make_booking(booking_in: BookingIn):
  ##  user_in_db = get_user(booking_in.username)
    ##if user_in_db == None:
      ##  raise HTTPException(status_code=404,
        ##                    detail="El usuario no existe")
    ##user_in_db.balance = user_in_db.balance - booking_in.value
    ##update_user(user_in_db)
    ##booking_in_db = BookingInDB(**booking_in.dict(),##MAPING
      ##                      actual_balance = user_in_db.balance)
    ##booking_in_db = save_booking(booking_in_db)
    ##booking_out = BookingOut(**booking_in_db.dict())
    ##return booking_out