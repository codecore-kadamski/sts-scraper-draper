
-- CREATE TABLE IF NOT EXISTS sports (
--     -- id int 
--     sts_id int, 
--     name varchar(100),
--     url varchar(400),
--     PRIMARY KEY (name),
--     UNIQUE (name, sts_id, url)
-- );

CREATE TABLE IF NOT EXISTS "sports" (
    "id" serial,
    "sts_id" numeric(9,2),
    "name" varchar(400),
    "url" varchar(400),
    PRIMARY KEY( id ),
    UNIQUE (name, sts_id, url)
);