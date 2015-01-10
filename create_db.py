# -*- coding: utf-8 -*-
import sqlite3
con = sqlite3.connect("data.db")
sql = u"""
create table db_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    , screen_name varchar(20)
    , timestamp TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
);
"""
con.execute(sql)
con.close()
