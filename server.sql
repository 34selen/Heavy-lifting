-- your_script.sql
-- 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS heavy_lift;

-- 데이터베이스 사용
USE heavy_lift;

DROP TABLE IF EXISTS users;
DROP TABLE IF EXISTS records;

-- users 테이블 생성
CREATE TABLE IF NOT EXISTS users (
    uid INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    id VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(100) NOT NULL
);

-- records 테이블 생성
CREATE TABLE IF NOT EXISTS records (
    record_id INT AUTO_INCREMENT PRIMARY KEY,
    uid INT,
    id VARCHAR(100) NOT NULL,
    record_text VARCHAR(255),
    FOREIGN KEY (uid) REFERENCES users(uid) ON DELETE CASCADE
);

-- users 테이블에 예시 데이터 삽입
INSERT INTO users (name, id, password) VALUES
('Alice', 'alice123', 'password1'),
('Bob', 'bob234', 'password2'),
('Charlie', 'charlie345', 'password3');

-- records 테이블에 예시 데이터 삽입
INSERT INTO records (uid, id, record_text) VALUES
(1, 'alice123', 'Bench press: 80kg'),
(2, 'bob234', 'Deadlift: 120kg'),
(3, 'charlie345', 'Squat: 100kg');