-- sql script


CREATE DATABASE IF NOT EXISTS Journify_db;
       CREATE USER IF NOT EXISTS 'Journify_user'@'localhost' IDENTIFIED BY 'Journify_pwd';
              GRANT ALL PRIVILEGES ON Journify_db.* TO 'Journify_user'@'localhost';
                                      GRANT SELECT ON performance_schema.* TO 'Journify_user'@'localhost';
FLUSH PRIVILEGES;