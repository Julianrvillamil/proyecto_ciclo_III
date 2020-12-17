from pydantic import BaseModel
##ITS NOT THE TABLE, ITS A WAY TO CATCH THE INFORMATION
##WHAT WE ARE DOING IS LIKE AN ABSTRACTION OF THE MODEL IN THE TABLES OF THE DB
##ALSO WE ONLY BRING SOME THINGS, LIKE IN A SELECT QUERY, IN THIS CASE ONLY BRING NAME AND PASSWORD
    ##FOR THE INPUT (THAT WILL BE THE USER INPUT) AND THE OUTPUT (THE INFORMATION THAT WE WILL SHOW THE USER)
class UserIn(BaseModel):
    username: str
    password: str
class UserOut(BaseModel):
    username: str
    name: str
    lastname: str
    document: str
    rank: str