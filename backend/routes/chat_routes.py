from flask import Blueprint,render_template,request,session,redirect
from models.chat_model import save_message,get_messages
from models.connection_model import is_connected
from models.chat_model import get_chat_users

chat_bp = Blueprint('chat',__name__)

@chat_bp.route('/chat/<user>')
def chat(user):

    if not is_connected(session['user'],user):
        return "Chat available only after mentor request accepted"

    messages=get_messages(session['user'],user)

    return render_template(
        "chat.html",
        messages=messages,
        other=user
    )

@chat_bp.route('/send/<user>',methods=['POST'])

def send(user):

    message=request.form['message']

    save_message(session['user'],user,message)

    return redirect('/chat/'+user)

@chat_bp.route('/chat_list')

def chat_list():

    users = get_chat_users(session['user'])

    return render_template("chat_list.html",users=users)