CREATE TABLE IF NOT EXISTS users (
    id BIGINT UNIQUE NOT NULL,
    username VARCHAR(32) NOT NULL,
    discriminator VARCHAR(4) NOT NULL,
    avatar TEXT,
    app BOOLEAN DEFAULT FALSE NOT NULL,
    PRIMARY KEY (username, discriminator)
);

CREATE TABLE IF NOT EXISTS tokens (
    user_id BIGINT REFERENCES users(id) ON DELETE CASCADE ON UPDATE NO ACTION NOT NULL,
    expires_at TIMESTAMP WITHOUT TIME ZONE NOT NULL,
    token TEXT NOT NULL,
    data JSON NOT NULL,
    PRIMARY KEY (user_id)
);

CREATE TABLE IF NOT EXISTS files (
    id BIGINT UNIQUE NOT NULL,
    name TEXT NOT NULL,
    mimetype TEXT NOT NULL,
    data BYTEA NOT NULL
);

CREATE TABLE IF NOT EXISTS assets (
    id BIGINT UNIQUE NOT NULL,
    name VARCHAR(64) NOT NULL,
    url_path TEXT NOT NULL,
    file_id BIGINT REFERENCES files(id) ON DELETE CASCADE ON UPDATE NO ACTION NOT NULL,
    creator_id BIGINT REFERENCES users(id) ON DELETE CASCADE ON UPDATE NO ACTION NOT NULL,
    PRIMARY KEY (url_path)
);

CREATE TABLE IF NOT EXISTS roles (
    id BIGINT NOT NULL,
    name VARCHAR(32) UNIQUE NOT NULL,
    position REAL NOT NULL,
    color INTEGER,
    permissions INTEGER DEFAULT (0) NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS userroles (
    user_id BIGINT REFERENCES users(id) ON DELETE CASCADE ON UPDATE NO ACTION NOT NULL,
    role_id BIGINT REFERENCES roles(id) ON DELETE CASCADE ON UPDATE NO ACTION NOT NULL,
    PRIMARY KEY (user_id, role_id)
);

CREATE TABLE IF NOT EXISTS challengelanguages (
    id BIGINT NOT NULL,
    name TEXT UNIQUE NOT NULL,
    download_url TEXT,
    disabled BOOLEAN DEFAULT FALSE NOT NULL,
    piston_lang TEXT NOT NULL,
    piston_lang_ver TEXT NOT NULL,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS challenges (
    id BIGINT NOT NULL,
    title TEXT NOT NULL,
    author_id BIGINT REFERENCES users(id) ON DELETE CASCADE ON UPDATE NO ACTION NOT NULL,
    description TEXT NOT NULL,
    language_ids BIGINT ARRAY NOT NULL,
    example_in TEXT ARRAY NOT NULL,
    example_out TEXT ARRAY NOT NULL,
    released_at TIMESTAMP WITHOUT TIME ZONE,
    PRIMARY KEY (id)
);

CREATE TABLE IF NOT EXISTS challengesubmissions (
    id BIGINT UNIQUE NOT NULL,
    challenge_id BIGINT REFERENCES challenges(id) ON DELETE CASCADE ON UPDATE NO ACTION NOT NULL,
    author_id BIGINT REFERENCES users(id) ON DELETE CASCADE ON UPDATE NO ACTION NOT NULL,
    language_id BIGINT REFERENCES challengelanguages(id) ON DELETE CASCADE ON UPDATE NO ACTION NOT NULL,
    code TEXT NOT NULL,
    PRIMARY KEY (challenge_id, author_id)
);

CREATE TABLE IF NOT EXISTS challengeparticipants (
    id BIGINT UNIQUE NOT NULL,
    challenge_id BIGINT REFERENCES challenges(id) ON DELETE CASCADE ON UPDATE NO ACTION NOT NULL,
    user_id BIGINT REFERENCES users(id) ON DELETE CASCADE ON UPDATE NO ACTION NOT NULL,
    PRIMARY KEY (challenge_id, user_id)
);


CREATE SEQUENCE IF NOT EXISTS global_snowflake_id_seq;

CREATE OR REPLACE FUNCTION create_snowflake()
    RETURNS bigint
    LANGUAGE 'plpgsql'
AS
$BODY$
DECLARE
    our_epoch  bigint := 1609459200;
    seq_id     bigint;
    now_millis bigint;
    -- the id of this DB shard, must be set for each
    -- schema shard you have - you could pass this as a parameter too
    shard_id   int    := 1;
    result     bigint := 0;
BEGIN
    SELECT nextval('global_snowflake_id_seq') % 1024 INTO seq_id;

    SELECT FLOOR(EXTRACT(EPOCH FROM clock_timestamp()) * 1000) INTO now_millis;
    result := (now_millis - our_epoch) << 22;
    result := result | (shard_id << 9);
    result := result | (seq_id);
    return result;
END;
$BODY$;

CREATE OR REPLACE FUNCTION snowflake_to_timestamp(flake BIGINT)
    RETURNS TIMESTAMP
    LANGUAGE 'plpgsql'
AS
$BODY$
DECLARE
    our_epoch  bigint := 1609459200;
BEGIN
    RETURN to_timestamp(((flake >> 22) + our_epoch) / 1000);
END;
$BODY$;
