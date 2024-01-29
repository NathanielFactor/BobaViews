from flask import Flask, request, url_for, redirect, session, render_template, jsonify
from flask import session
import time
import datetime
import numpy as np
import htmloperations as htop

app = Flask(__name__)
app.secret_key = "super-secret-key"
app.config['SESSION_COOKIE_NAME'] = 'spotify-login-session'
TOKEN_INFO = 'token_info'
CLIENT_ID = "e454cfe7332648138c6cd894bede3ea9"
CLIENT_SECRET = "dfb2a085a05e4a71bfa60d263a5e4d45"
user_id = "nfac"

def get_current_year():
    current_year = datetime.datetime.now().year
    return (current_year)

def get_current_month():
    current_month = datetime.datetime.now().month
    return (current_month)

def get_message_by_date(date):
    JOURNAL_ENTRIES = htop.get_messages_by_month(user_id, get_current_year(), get_current_month())
    print(JOURNAL_ENTRIES)
    for entry in JOURNAL_ENTRIES:
       print (entry)
       if entry[3] == date:
           return entry[2]
    return None

def get_mood_by_date(date):
    JOURNAL_ENTRIES = htop.get_messages_by_month(user_id, get_current_year(), get_current_month())
    for entry in JOURNAL_ENTRIES:
       if entry[3] == date:
           return entry[1]
    return None

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/calendar')
def calendar():
    try:
        token_info = get_token()
    except:
        print("User not logged in")
        return redirect(url_for('login'))
    return render_template('calendar.html',
                           
                           )
@app.route('/submit', methods=['POST'])
def submit_entry():
    data = request.json
    date = data.get('date')
    concatenated_values = data.get('concatenatedValues')
    htop.addMessage(user_id, concatenated_values, date)
    # Save to database (example code, depends on your database setup)
    return jsonify({"success": True, "message": "Data saved successfully."})

@app.route('/get_message')
def get_message():
    try:
        token_info = get_token()
    except:
        print("User not logged in")
        data = {'message': 'login'}
        return jsonify(data)
    
    date = request.args.get('date')
    message = get_message_by_date(date)
    mood = get_mood_by_date(date)  
    
    if message:
        data ={'message': message, 'mood': mood}
        return jsonify(data)  # Assuming the column name is 'content'
    else:
        data = {'message': 'No message for this date'}
        return jsonify(data)

@app.route('/journal')
def journal():
    try:
        token_info = get_token()
    except:
        print("User not logged in")
        return redirect(url_for('login'))
    return render_template('journal.html',
                           
                           )



@app.route('/about_us')
def aboutUs():
    try:
        token_info = get_token()
    except:
        print("User not logged in")
        return redirect(url_for('login'))

    return render_template('about_us.html', id=id)
                           

@app.route('/login')
def login():
     return render_template('login.html')

@app.route('/callback')
def callback():
    return redirect(url_for('index'))


def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        redirect(url_for('login'))
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    

if __name__ == '__main__':
    app.run(debug=True)