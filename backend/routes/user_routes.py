from flask import Blueprint,render_template,session,request,redirect
from models.user_model import search_users
from models.user_model import get_user
from utils.db import get_db
from models.videos_model import get_videos
from models.user_model import get_user_by_username
from models.connection_model import send_request
from models.connection_model import get_received_requests
from models.connection_model import accept_request, reject_request
from models.chat_model import get_chat_users
from models.connection_model import get_requested_mentors


user_bp = Blueprint('user',__name__)

@user_bp.route('/dashboard')

def dashboard():

    username = session.get('user')

    return render_template(
        "dashboard.html",
        username=username
    )


@user_bp.route('/search',methods=['POST'])
def search():

    skill=request.form['skill']

    users=search_users(skill)

    if users:
        return render_template(
        "dashboard.html",
        users=users
        )

    else:

        videos=get_videos(skill)

        return render_template(
        "dashboard.html",
        videos=videos
        )

@user_bp.route('/profile')
def profile():

    username = session['user']

    user = get_user_by_username(username)

    requests = get_received_requests(username)

    chats = get_chat_users(username)

    mentors = get_requested_mentors(username)

    return render_template(
        "profile.html",
        user=user,
        requests=requests,
        chats=chats,
        mentors=mentors
    )

@user_bp.route('/edit_profile',methods=['POST'])

def edit_profile():

    from utils.db import get_db

    conn=get_db()

    conn.execute("""

    UPDATE users

    SET email=?,phone=?,education=?,skill=?

    WHERE username=?

    """,(request.form['email'],
    request.form['phone'],
    request.form['education'],
    request.form['skill'],
    session['user']))

    conn.commit()

    return redirect('/profile')

@user_bp.route('/change_password',methods=['POST'])

def change_password():

    from utils.db import get_db

    conn=get_db()

    conn.execute("""

    UPDATE users SET password=?

    WHERE username=?

    """,(request.form['new'],session['user']))

    conn.commit()

    return redirect('/profile')

@user_bp.route('/delete_account')

def delete_account():

    from utils.db import get_db

    conn=get_db()

    conn.execute("DELETE FROM users WHERE username=?",(session['user'],))

    conn.commit()

    session.clear()

    return redirect('/')


from models.connection_model import get_request_status

@user_bp.route('/mentor/<username>')
def mentor_page(username):

    from utils.db import get_db

    conn=get_db()

    user=conn.execute(
    "SELECT * FROM users WHERE username=?",(username,)
    ).fetchone()

    status=get_request_status(session['user'],username)

    conn.close()

    return render_template(
        "mentor.html",
        user=user,
        status=status
    )

from models.connection_model import send_request

@user_bp.route('/send_request/<mentor>/<req_type>')
def send_request_route(mentor,req_type):

    send_request(session['user'],mentor,req_type)

    return redirect('/mentor/'+mentor)



@user_bp.route('/accept_request/<int:id>')
def accept(id):

    accept_request(id)

    return redirect('/profile')