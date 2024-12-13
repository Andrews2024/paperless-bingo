CREATE TABLE player (
    name TEXT PRIMARY KEY
);

CREATE TABLE entry (
    id UUID PRIMARY KEY,
    value TEXT NOT NULL
);

CREATE TABLE user_entry (
    name TEXT REFERENCES player (name),
    entry UUID REFERENCES entry (id)
);

CREATE TABLE user_board (    
    id UUID PRIMARY KEY,
    name TEXT REFERENCES player (name)
);

CREATE TABLE board_entry (
    id UUID PRIMARY KEY,
    name TEXT REFERENCES player (name),
    entry UUID REFERENCES entry (id),
    is_checked BOOL DEFAULT FALSE,
    board_id UUID REFERENCES user_board (id)
);