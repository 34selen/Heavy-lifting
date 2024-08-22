from flask import Flask, render_template, request, redirect, url_for
import MySQLdb
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user

app = Flask(__name__)
app.secret_key = 'your_secret_key'

# MySQL 설정
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'gkskgksj0!',
    'db': 'heavy_lift'
}

FLAG = 'FAKEFLAG'

# Flask-Login 설정
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

# 사용자 모델
class User(UserMixin):
    def __init__(self, uid, name, id, password):
        self.uid = uid
        self.name = name
        self.id = id
        self.password = password

@login_manager.user_loader
def load_user(user_id):
    conn = MySQLdb.connect(**db_config)
    cur = conn.cursor()
    cur.execute("SELECT * FROM users WHERE id = %s", (user_id,))
    user = cur.fetchone()
    cur.close()
    conn.close()
    if user:
        return User(uid=user[0], name=user[1], id=user[2], password=user[3])
    return None

@app.route('/')
@login_required
def index():
    # 현재 로그인된 사용자의 기록만 조회합니다.
    conn = MySQLdb.connect(**db_config)
    cur = conn.cursor()
    cur.execute("SELECT record_text FROM records WHERE id = %s", (current_user.id,))
    records = cur.fetchall()
    cur.close()
    conn.close()
    print(records)
    return render_template('index.html', records=records, user=current_user.name)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']

        conn = MySQLdb.connect(**db_config)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and user[3] == password:
            login_user(User(uid=user[0], name=user[1], id=user[2], password=user[3]))
            return redirect(url_for('index'))
        
        return "Invalid credentials. Please try again."

    return render_template('login.html')

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/add_record', methods=['POST'])
@login_required
def add_record():
    if request.method == 'POST':
        record_text = request.form['record_text']

        conn = MySQLdb.connect(**db_config)
        cur = conn.cursor()
        cur.execute("INSERT INTO records (id, record_text) VALUES (%s, %s)", (current_user.id, record_text))
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('index'))

@app.route('/debug', methods=['GET', 'POST'])
def debug():
    if request.method == 'POST':
        id = request.form['id']
        password = request.form['password']

        conn = MySQLdb.connect(**db_config)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users WHERE id = %s", (id,))
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and user[3] == password:
            login_user(User(uid=user[0], name=user[1], id=user[2], password=user[3]))
            return redirect(url_for('index'))
        
        return "Invalid credentials. Please try again."
    else:
        conn = MySQLdb.connect(**db_config)
        cur = conn.cursor()
        cur.execute("SELECT * FROM users")
        user = cur.fetchone()
        cur.close()
        conn.close()
        return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)
