-- Create challenge schema
CREATE SCHEMA challenge AUTHORIZATION squadmakers_admin;

GRANT USAGE ON SCHEMA challenge TO squadmakers;

GRANT SELECT ON ALL TABLES IN SCHEMA challenge TO squadmakers;
GRANT USAGE, SELECT ON ALL SEQUENCES IN SCHEMA challenge TO squadmakers;

ALTER DEFAULT PRIVILEGES IN SCHEMA challenge
    GRANT SELECT ON TABLES TO squadmakers;
ALTER DEFAULT PRIVILEGES IN SCHEMA challenge
    GRANT USAGE, SELECT ON SEQUENCES TO squadmakers;
