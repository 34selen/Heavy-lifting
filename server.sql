-- your_script.sql
-- 데이터베이스 생성
CREATE DATABASE IF NOT EXISTS heavy_lift;

CREATE USER IF NOT EXISTS 'appuser'@'%' IDENTIFIED BY 'app_password';
GRANT ALL PRIVILEGES ON heavy_lift.* TO 'appuser'@'%';
FLUSH PRIVILEGES;
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
('admin', 'admin', 'admin'),
('guest', 'guest', 'guest'),
('selen', 'selen', 'selen');

-- records 테이블에 예시 데이터 삽입
INSERT INTO records (uid, id, record_text) VALUES
(1, 'admin', 'Cykor{selenIsGood}'),
(2, 'guest', 'Squat: 100kg'),
(3, 'selen', 'Deadlift: 120kg');

select * from users;