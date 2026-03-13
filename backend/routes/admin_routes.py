from flask import Blueprint,render_template,request,redirect,session
from models.skill_model import add_skill,get_skills,delete_skill
from models.user_model import get_all_users
from models.videos_model import get_db

admin_bp = Blueprint('admin',__name__)

ADMIN_USER="admin"
ADMIN_PASS="admin123"


@admin_bp.route('/admin',methods=['GET','POST'])

def admin_login():

    if request.method=="POST":

        if request.form['username']==ADMIN_USER and request.form['password']==ADMIN_PASS:

            return redirect('/admin_dashboard')

    return render_template("login.html")


@admin_bp.route('/admin_dashboard')

def admin_dashboard():
    if 'admin' not in session:
        return redirect('/login')
    
    users=get_all_users()
    skills = get_skills()

    return render_template("admin_dashboard.html",users=users,skills=skills)


@admin_bp.route('/view_users')

def view_users():

    users=get_all_users()

    return render_template("admin_dashboard.html",users=users)


@admin_bp.route('/add_skill',methods=['POST'])
def add_skill():

    conn=get_db()

    conn.execute("""

    INSERT INTO skills(skill_name,title,link)

    VALUES(?,?,?)

    """,(request.form['skill'],
    request.form['title'],
    request.form['link']))

    conn.commit()

    conn.close()

    return redirect('/admin_dashboard')

@admin_bp.route('/view_skills')

def view_skills():

    skills=get_skills()

    return render_template("admin_dashboard.html",skills=skills)


@admin_bp.route('/delete_skill/<id>')

def delete_skill_route(id):

    delete_skill(id)

    return redirect('/view_skills')