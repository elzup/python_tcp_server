# -*- coding: utf-8 -*-
import sqlite3
class LogModel():
    con = sqlite3.connect("data.db")
#    def __init__(self):

    def __del__(self):
        self.con.close()

    def Initialize(self):
        sql = u"""
create table IF NOT EXISTS db_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    , screen_name varchar(20)
    , timestamp TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
);
"""
        self.con.execute(sql)
        self.con.commit()

    def Reset(self):
        sql = u"DROP TABLE db_log;"
        self.con.execute(sql)
        self.Initialize()
        self.con.commit()

    def InsertLog(self, sn):
        sql = u"insert into db_log (screen_name) values (?)"
        self.con.execute(sql, (sn,))
        self.con.commit();

    def SelectLog(self):
        sql = u"select * from db_log"
        res = self.con.execute(sql)
        return res

#    def SelectLog(self):

if __name__ == '__main__':
    lm = LogModel()
    lm.Initialize()
    lm.InsertLog("hoge")
    res = lm.SelectLog()
    print (res.fetchall())

