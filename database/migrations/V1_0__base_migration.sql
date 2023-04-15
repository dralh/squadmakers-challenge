CREATE FUNCTION challenge.update_modified_column() RETURNS TRIGGER
    LANGUAGE PLPGSQL
AS
$$
BEGIN
    IF ROW (NEW.*) IS DISTINCT FROM ROW (OLD.*) THEN
        NEW.updated_at = NOW();
        RETURN NEW;
    ELSE
        RETURN OLD;
    END IF;
END;
$$;

ALTER FUNCTION challenge.update_modified_column() OWNER TO squadmakers_admin;

------------- Joke
CREATE TABLE challenge.joke
(
    joke_id    BIGSERIAL CONSTRAINT pk_joker_id PRIMARY KEY,
    content     VARCHAR                                NOT NULL,
    created_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL,
    updated_at TIMESTAMP WITH TIME ZONE DEFAULT NOW() NOT NULL
);

ALTER TABLE challenge.joke
    OWNER TO squadmakers_admin;


GRANT SELECT, DELETE, INSERT, UPDATE ON challenge.joke TO sm_challenge;

CREATE TRIGGER tg_user_update
    BEFORE UPDATE
    ON challenge.joke
    FOR EACH ROW
EXECUTE PROCEDURE challenge.update_modified_column();
