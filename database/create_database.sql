CREATE ROLE squadmakers;
CREATE USER squadmakers_admin WITH
    NOSUPERUSER
    NOCREATEDB
    PASSWORD 'pass123'
    IN ROLE squadmakers;

CREATE DATABASE squadmakers WITH OWNER squadmakers_admin;
GRANT CONNECT ON DATABASE squadmakers TO squadmakers;
