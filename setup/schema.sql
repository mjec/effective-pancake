DROP TABLE IF EXISTS users;
CREATE TABLE users (
    id integer primary key autoincrement,
    username text not null,
    password text not null,
    email text null
);

DROP TABLE IF EXISTS todo_items;
CREATE TABLE todo_items (
    id integer primary key autoincrement,
    name text not null,
    details text null,
    parent_id integer null,
    created timestamp not null,
    due timestamp null,
    status int not null
);

DROP TABLE IF EXISTS files;
CREATE TABLE files (
    id integer primary key autoincrement,
    todo_item_id integer not null,
    filename text not null
);


DROP TABLE IF EXISTS comments;
CREATE TABLE comments (
    id integer primary key autoincrement,
    todo_item_id integer null,
    created timestamp not null,
);
