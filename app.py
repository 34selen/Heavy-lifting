from flask import Flask, render_template, request, redirect, url_for
import MySQLdb
import binascii
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
import util
import os

app = Flask(__name__)
app.secret_key = binascii.hexlify(os.urandom(24)).decode()

# MySQL 설정
db_config = {
    'host': 'localhost',
    'user': 'root',
    'password': 'password',
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
    cur.execute("SELECT record_text FROM records WHERE id = %s",(current_user.id,))
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
        if(util.filter(id) or util.filter(password)):
            return '필터링됨'
        cur.execute(f"SELECT * FROM users WHERE id ='{id}' and password= '{password}'")   # 여기가 취약점임
        user = cur.fetchone()
        cur.close()
        conn.close()

        if user and user[3] == password:
            login_user(User(uid=user[0], name=user[1], id=user[2], password=user[3]))
            return redirect(url_for('index'))
        error_message = "아이디 또는 비밀번호가 올바르지 않습니다. 다시 시도해 주세요."
        return render_template('login.html', error=error_message)

    return render_template('login.html')

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        user_id = request.form['id']
        password = request.form['password']

        conn = MySQLdb.connect(**db_config)
        cur = conn.cursor()

        # id 중복 확인
        cur.execute("SELECT COUNT(*) FROM users WHERE id = %s", (user_id,))
        count = cur.fetchone()[0]
        if count > 0:
            # id가 이미 존재하는 경우
            cur.close()
            conn.close()
            error_message = "이미 존재하는 ID입니다."
            return render_template('register.html', error=error_message)

        # id가 중복되지 않으면 사용자 정보 삽입
        cur.execute("INSERT INTO users (name, id, password) VALUES (%s, %s, %s)", (name, user_id, password))
        conn.commit()

        cur.close()
        conn.close()

        return redirect(url_for('login'))

    return render_template('register.html')
@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/add_record', methods=['GET','POST'])
@login_required
def add_record():
    if request.method == 'POST':
        record_text = request.form['record_text']

        conn = MySQLdb.connect(**db_config)
        cur = conn.cursor()
        cur.execute("INSERT INTO records (id, record_text) VALUES (%s, %s)",(current_user.id,record_text))
        conn.commit()
        cur.close()
        conn.close()

        return redirect(url_for('index'))
    return render_template('add_record.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8000)
