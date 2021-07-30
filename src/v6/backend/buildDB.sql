use pingerator;

-- Updated manualy
-- ip lookup:
    -- id
    -- test_time_id fk > testtime table
    -- domain name
    -- 
CREATE table ipLookup(
    id SERIAL NOT NULL,
    time_created TIMESTAMP NOT NULL,
    ipv4 VARCHAR(15),
    domain_name VARCHAR(80),
    PRIMARY KEY(id),
    UNIQUE(id));
-- incidint table

-- testtime table 
    -- id primary
    -- datetime
    -- 

CREATE table testTime(
    id SERIAL NOT NULL,
    datetime_tested TIMESTAMP NOT NULL,
    PRIMARY KEY(id),
    UNIQUE(test_time_id));

-- We need a table for the speeds
    -- test_time_id fk > testtime table
    -- we need speed value
    -- we need ip address
CREATE table speed (
    test_time_id INT NOT NULL,
    downspeed_value DOUBLE NULL,
    upspeed_value DOUBLE NULL,
    CONSTRAINT test_time_id
        FOREIGN KEY(test_time_id)
        REFERENCES testTime (test_time_id)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT);

CREATE table pings (
    test_time_id INT NOT NULL,
    pingresponse_value FLOAT NULL,
    upspeed_value DOUBLE NULL,
    ipv4_id INT NOT NULL,
    CONSTRAINT test_time_id
        FOREIGN KEY(test_time_id)
        REFERENCES testTime (id)
        ON DELETE RESTRICT
        ON UPDATE RESTRICT,
    CONSTRAINT ipv4_id
        FOREIGN KEY(ipv4_id)
        REFERENCES ipLookup (id));
-- we need a table for the pings
    -- test_time_id fk > testtime table
    -- we need ping response time or NULL if none
    -- we need id of domain name given the appropriate IP


