from connection.models import Account
from connection.connect import Session
from werkzeug.security import check_password_hash

session = Session()

def login_account(login_username, login_password):
    login_account = session.query(Account).filter_by(username=login_username).first()

    if login_account and check_password_hash(login_account.password, login_password):
        print("Success")
        return login_account
    else:
        print("Something Went Wrong")
        return False
    
  