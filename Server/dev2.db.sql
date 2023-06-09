BEGIN TRANSACTION;
CREATE TABLE IF NOT EXISTS "level" (
	"id"	INTEGER,
	"title"	VARCHAR(255),
	"sentence"	MEDIUMTEXT,
	"difficulty"	INTEGER DEFAULT 1,
	"score"	INTEGER DEFAULT 100,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "room" (
	"id"	INTEGER,
	"max"	INTEGER DEFAULT 2,
	PRIMARY KEY("id" AUTOINCREMENT)
);
CREATE TABLE IF NOT EXISTS "user" (
	"id"	INTEGER,
	"name"	VARCHAR(255) NOT NULL,
	"username"	VARCHAR(255) NOT NULL,
	"password"	VARCHAR(255) NOT NULL,
	"current_room"	INTEGER DEFAULT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("current_room") REFERENCES "room"("id")
);
CREATE TABLE IF NOT EXISTS "completed_levels" (
	"id"	INTEGER,
	"score"	INTEGER,
	"userId"	INTEGER NOT NULL,
	"levelId"	INTEGER NOT NULL,
	PRIMARY KEY("id" AUTOINCREMENT),
	FOREIGN KEY("userId") REFERENCES "user"("id"),
	FOREIGN KEY("levelId") REFERENCES "level"("id")
);
COMMIT;
