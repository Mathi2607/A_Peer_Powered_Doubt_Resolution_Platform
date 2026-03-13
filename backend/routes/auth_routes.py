from flask import Blueprint,render_template,request,redirect,session
from models.user_model import create_user,get_user

auth_bp = Blueprint('auth',__name__)

ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

@auth_bp.route('/')
def splash():
    return render_template("splash.html")

@auth_bp.route('/welcome')
def welcome():
    return render_template("welcome.html")

@auth_bp.route('/login',methods=['GET','POST'])
def login():

    if request.method=='POST':

        username=request.form['username']
        password=request.form['password']

        if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:
            session['admin'] = True
            return redirect('/admin_dashboard')

        user=get_user(username,password)

        if user:
            session['user']=username
            return redirect('/dashboard')
        
        else:
            return render_template("login.html",error="Invalid credentials")

    return render_template("login.html")


@auth_bp.route('/signup',methods=['GET','POST'])
def signup():

    if request.method=='POST':

        username=request.form['username']
        email=request.form['email']
        phone=request.form['phone']
        education=request.form['education']
        skill=request.form['skill']
        password=request.form['password']

        create_user(username,email,phone,education,skill,password)

        return redirect('/login')

    return render_template("signup.html")



@auth_bp.route('/logout')

def logout():

    session.clear()

    return redirect('/')