# Design
## User Actions
### Add user
1. Click `Add User`
2. Enter name of user (must be unique)

### Select User
1. Select user from drop down
2. Set user variable for selecting entries

### Click Square
1. Click square after event happens
2. Square is set to `true`
3. Clicking square again sets it back to `false`

### Add Entry
1. Click `Add Entry`
2. Enter name of person associated with event (dropdown)
3. Enter description of the event (text entry)
4. Click `Submit`

## App Acions
### Detect Bingo
1. Check rows for 5 `true`
2. Check columns for 5 `true`
3. Check LR and RL diagonals for 5 `true`

### Generate Bingo Board
1. Gather entries where name != user name
2. Randomize order
3. Select 24 entries
4. Select a FREE SQUARE entry
5. Submit entries to HTML template

## Database Design
```
CREATE TABLE User {
    name TEXT,
}

CREATE TABLE Entries {
    name TEXT,
    value TEXT,
    isFree BOOL,
    PRIMARY KEY (name, value),
    FOREIGN KEY (name) REFERENCES (User.name)
}
```