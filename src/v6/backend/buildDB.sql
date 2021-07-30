use pingerator;

-- We need a table for the speeds
    -- test_time_id fk > testtime table
    -- we need speed value
    -- we need ip address
CREATE table speed (
    datetime_tested TIMESTAMP NOT NULL,
    downspeed_value DOUBLE NULL,
    upspeed_value DOUBLE NULL,

)

CREATE table pings (
    
)
-- we need a table for the pings
    -- test_time_id fk > testtime table
    -- we need ping response time or NULL if none
    -- we need id of domain name given the appropriate IP


-- Updated manualy
-- ip lookup:
    -- id
    -- test_time_id fk > testtime table
    -- domain name
    -- 

-- incidint table

-- testtime table 
    -- id primary
    -- datetime
    -- 