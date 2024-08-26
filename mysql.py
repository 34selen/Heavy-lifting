import MySQLdb

# MySQL에 연결
db = MySQLdb.connect(host="localhost", user="root", passwd="gkskgksj0!", db="heavy_lift")

# 커서 객체를 가져옵니다
cursor = db.cursor()

# server.sql 파일을 열고 실행합니다
with open('./server.sql', 'r') as file:
    sql = file.read()
    cursor.execute(sql)

# 커밋하여 변경 사항 저장
db.commit()

# 연결 닫기
db.close()