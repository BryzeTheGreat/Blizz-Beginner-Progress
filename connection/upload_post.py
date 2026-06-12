from connection.connect import Session
import uuid
from connection.models import UploadPost

session = Session()

def save_post_data(username, content, filename):
    post_id = str(uuid.uuid4())

    post = UploadPost(post_id=post_id, content=content, image=filename, username=username)

    session.add(post)

    session.commit()
def load_post_data():
    Post = session.query(UploadPost).all()
    return Post

