-- schema.sql

DROP TABLE IF EXISTS BobaViews;

CREATE TABLE IF NOT EXISTS BobaViews (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    userName TEXT NOT NULL,
    PasswordID TEXT NOT NULL,
    Streak INTEGER NOT NULL,
)
    