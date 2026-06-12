from flask import Blueprint, render_template, redirect, url_for, session, request, current_app
import os
from werkzeug.utils import secure_filename
from connection.upload_post import save_post_data
from connection.models import UploadPost
from connection.connect import Session



db_session = Session()
homepage = Blueprint('homepage', __name__)

@homepage.route('/homepage', methods=['GET', 'POST'])
def home():
    if not session.get('logged_in'):
        return redirect(url_for('frontpage.front'))
    

    post_data = db_session.query(UploadPost).all()

    
    if request.method == "POST":
        user_id = session['user_id']
        username = session['username']
        text_content = request.form.get('post_content')
        file = request.files.get('post_image')

        if file and file.filename != '':
            filename = secure_filename(file.filename)

            upload_path = current_app.config['UPLOAD_FOLDER']

            destination = os.path.join(upload_path, filename)
            file.save(destination)

        save_post_data(username, text_content, file.filename)

        return redirect(url_for('homepage.home'))

    
    return render_template('homepage.html', feed_posts=post_data)