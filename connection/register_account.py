from connection.connect import Session
from connection.models import Account
import uuid
from werkzeug.security import generate_password_hash

session = Session()

def username_duplication(verify_username):
    result = session.query(Account).filter_by(username=verify_username).first()
    if result:
        return True
    else:
        return False
    
def register_account(new_username, new_password):
    if username_duplication(new_username):
        print("Something Went Wrong!")
        return False
    else:
        uid = str(uuid.uuid4())
        hash_password = generate_password_hash(new_password)
        new_user = Account(account_id=uid, username=new_username, password=hash_password, name=new_username)

        session.add(new_user)

        session.commit()
        print("Account Created!")
        return True
    
 