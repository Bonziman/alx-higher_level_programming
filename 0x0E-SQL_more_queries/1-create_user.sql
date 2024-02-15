--script to create a user and grant it all privileges
CRATE USER 'user_0d_1' IDENTIFIED BY 'user_0d_1_pwd' IF NOT EXISTS;
GRANT ALL PRIVILEGES ON *.* TO 'user_0d_1' WITH GRANT OPTION;
