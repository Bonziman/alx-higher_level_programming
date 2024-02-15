--script to create a user and grant it all privileges
CREATE USER IF NOT EXISTS 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd';
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1' WITH GRANT OPTION;
