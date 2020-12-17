from typing import Dict
from pydantic import BaseModel
##THE DEFINITION OF THE TABLES IN THE DATA BASE
class UserInDB(BaseModel):
    username: str
    password: str
    username: str
    name: str
    lastname: str
    document: str
    rank: str
###############################################


database_users = Dict[str, UserInDB]##CREATE THE DICTIONARY FOR THE USERS IN THE DB

##ACTUAL USERS IN THE DB
database_users = {
    "camilo24": UserInDB(**{"username":"camilo24",
                            "password":"root",
                            "name":"Camilo"
                            "lastname":"Rodríguez"
                            "document":"741852963"
                            "rank":"A"}),

    "andres18": UserInDB(**{"username":"andres18",
                            "password":"hola",
                            "name":"Andres"
                            "lastname":"Gómez"
                            "document":"852963741"
                            "rank":"B"}),
}
########################

##FUNCTION THAT SEARCH IF THE USER EXISTS, RETORN THE USER IF IS IT, OR RETURN NONE IF NOT
def get_user(username: str):
    if username in database_users.keys():
        return database_users[username]
    else:
        return None
##########################################################################################

##FUNCTION THAT UPDATE A USER 
def update_user(user_in_db: UserInDB):
    database_users[user_in_db.username] = user_in_db##IF THE USER EXITS OVERWRITE IT, IF DOESNT CREATE IT
    return user_in_db 
#because fast-api we use typing blabla: (var/obj)