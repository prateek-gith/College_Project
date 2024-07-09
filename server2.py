from flask import Flask, render_template, request,session,redirect
from flask_sqlalchemy import SQLAlchemy
import json
from flask_mail import Mail
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

User_Email="NULL"
Create_Pass="NULL"

with open ('config.json','r') as c:
    params=json.load(c)["params"]
    
local_server=True

app = Flask(__name__)
app.secret_key='Prateek-Secret-Key'

app.config.update(
    MAIL_SERVER='smtp.gmail.com',
    MAIL_PORT='465',
    MAIL_USE_SSL=True,
    MAIL_USERNAME=params['gmail_user'],
    MAIL_PASSWORD=params['gmail_pass']
)
Mail=Mail(app)

if (local_server):
    app.config['SQLALCHEMY_DATABASE_URI'] = params['local_uri']
else :
    app.config['SQLALCHEMY_DATABASE_URI'] = params['pro_uri']
    
db = SQLAlchemy(app)


class be_our_guest(db.Model):
    # G_Name=Name, G_EMail=Email, G_Date=Date, G_People=People, G_People=Type,G_Special=Special
    L_S_No = db.Column(db.Integer, primary_key=True, nullable=False)
    G_Name = db.Column(db.String(50), nullable=False)
    G_Date = db.Column(db.String(50), nullable=False)
    G_People = db.Column(db.Integer, nullable=False)
    G_Special = db.Column(db.String(100), nullable=False)
    G_People = db.Column(db.String(20), nullable=False)
    G_EMail = db.Column(db.String(100), nullable=False)
    G_Type = db.Column(db.String(20), nullable=False)

class login_user_data(db.Model):
    L_S_No = db.Column(db.Integer, primary_key=True, nullable=False)
    L_Name = db.Column(db.String(20), nullable=False)
    L_Phone_Number = db.Column(db.String(20), nullable=False)
    L_E_Mail = db.Column(db.String(20), nullable=False)
    L_Pass = db.Column(db.String(20), nullable=False)
    L_Con_Pass = db.Column(db.String(20), nullable=False)
    
class membership_table(db.Model):
    M_S_No = db.Column(db.Integer, nullable=False)
    M_Name = db.Column(db.String(20), nullable=False)
    M_E_Mail = db.Column(db.String(20), primary_key=True, nullable=False)
    M_Start_Date = db.Column(db.String(20), nullable=False)
    M_No_Months = db.Column(db.Integer, nullable=False)
    M_Address = db.Column(db.String(50), nullable=False)
    M_CIty = db.Column(db.String(10), nullable=False)
    M_State = db.Column(db.String(10), nullable=False)
    M_Pin_Code = db.Column(db.Integer, nullable=False)
    M_Menu_Type = db.Column(db.String(10), nullable=False)
    M_Phone = db.Column(db.String(13), nullable=False)
    
    
@app.route("/",methods=['GET', 'POST'])
def index():
    if (request.method == 'POST'):
        '''Add Entry To Database'''
        dtaa=login_user_data.query.filter_by().all()
        # global User_Email
        User_Email = request.form.get('User_Email')
        # global Create_Pass
        Create_Pass = request.form.get('Create_Pass')
        for login in dtaa:
            if (User_Email==login.L_E_Mail and Create_Pass==login.L_Pass):
                session['user']=User_Email
                return render_template('Home.html', params=params)
        return render_template('index.html', params=params,dtaa=dtaa)
    else : 
        return render_template('index.html', params=params)


@app.route("/login",methods=['GET', 'POST'])
def login():
    if (request.method == 'POST'):
        '''Add Entry To Database'''
        user_name = request.form.get('user_name')
        User_Email = request.form.get('User_Email')
        User_Num = request.form.get('User_Num')
        Create_Pass = request.form.get('Create_Pass')
        Confirm_Pass = request.form.get('Confirm_Pass')
        # S_No 	Name 	E_Mail 	Date_Time 	People 	Reques
        entry = login_user_data(L_Name=user_name, L_E_Mail=User_Email, L_Phone_Number=User_Num, L_Pass=Create_Pass, L_Con_Pass=Confirm_Pass)
        if(Create_Pass==Confirm_Pass):
            db.session.add(entry)
            db.session.commit()
    return render_template('login_Page_2.html', params=params)


@app.route("/about")
def about():
    return render_template('about.html', params=params)



@app.route("/contact")
def contact():
    return render_template('contact.html', params=params)


@app.route("/Nonveg")
def menu():
    return render_template('Nonveg.html', params=params)


@app.route("/service")
def service():
    return render_template('service.html', params=params)


@app.route("/team")
def team():
    return render_template('team.html', params=params)


@app.route("/testimonial")
def testimonial():
    return render_template('testimonial.html', params=params)


@app.route("/guest", methods=['GET', 'POST'])
def guest():
    if (request.method == 'POST'):
        '''Add Entry To Database'''
        Name = request.form.get('Name')
        Email = request.form.get('EMail')
        Date = request.form.get('Date_Time')
        People = request.form.get('No_Plate')
        Type = request.form.get('Type')
        Special = request.form.get('Request')
        entry = be_our_guest(G_Name=Name, G_EMail=Email, G_Date=Date, G_People=People, G_Type=Type,G_Special=Special)
        db.session.add(entry)
        db.session.commit()
        Mail.send_message('New Message From : ' + Name ,
                          sender=Email, 
                          recipients=[params['gmail_user']],
                          body=f'Special Request : {Special} \n + Name Is {Name}  \n Email is {Email} + \n + Date Is {Date} + \n + People Is {People}' 
                          )
    # return render_template('booking.html', params=params)
    return render_template('guest.html', params=params)


@app.route("/home")
def home():
    return render_template('Home.html', params=params)


@app.route("/veg")
def veg():
    return render_template('veg.html', params=params)


@app.route("/profile")
def profile():
    if 'user' in session:
        user_email = session['user']
        dta = login_user_data.query.filter_by(L_E_Mail=user_email).first()
        dta2 = membership_table.query.filter_by(M_E_Mail=user_email).first()
        if dta:
            return render_template('Profile.html', params=params, user_data=dta, User2_Data=dta2)
    return redirect('/')  # Redirect to login if user is not logged in


@app.route("/member", methods=['GET', 'POST'])
def member():
    if (request.method == 'POST'):
        '''Add Entry To Database'''
        name = request.form.get('name')
        Email = request.form.get('email')
        date = request.form.get('date')
        select1 = request.form.get('select1')
        address = request.form.get('address')
        city = request.form.get('city')
        state = request.form.get('state')
        pincode = request.form.get('pincode')
        select2 = request.form.get('select2')
        phone = request.form.get('phone')
        entry = membership_table(M_Name=name, M_E_Mail=Email, M_Start_Date=date, M_No_Months =select1, M_Address=address, M_CIty=city, M_State=state, M_Pin_Code=pincode, M_Menu_Type=select2, M_Phone=phone)
        db.session.add(entry)
        db.session.commit()
    return render_template('member.html', params=params)

@app.route("/edit/<string:sno>", methods=['GET', 'POST'])
def edit(sno):
    if ('user' in session):
        if request.method=='POST':
            name=request.form.get('name')
            email=request.form.get('email')
            Phone_Number=request.form.get('Phone_Number')
            Address=request.form.get('Address')
            
            if sno=='0':
                post=login_user_data(L_Name=name,L_Phone_Number=Phone_Number,L_E_Mail=email,Address=Address)
                db.session.add(post)
                db.session.commit()
            else :
                post=login_user_data.query.filter_by(L_E_Mail=sno).first()
                post.L_Name=name
                post.L_Phone_Number=Phone_Number
                post.L_E_Mail=email
                post_2=membership_table.query.filter_by(M_E_Mail=sno).first()
                if post_2 :
                    post_2.M_Address=Address
                db.session.commit()
                return redirect('/edit/'+sno)
        post=login_user_data.query.filter_by(L_E_Mail=sno).first()
        post_2=membership_table.query.filter_by(M_E_Mail=sno).first()
        return render_template('Edit.html',params=params,post=post,post_2=post_2)

@app.route("/logout")
def logout():
    session.pop('user', None)  # Clear the 'user' key from the session
    return redirect('/')  # Redirect to the home page after logout

# it automatic Dedect The changement in File
app.run(debug=True)
