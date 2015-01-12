# -*- coding: utf-8 -*-
import sqlite3


class LogModel():

    con = sqlite3.connect("data.db")
#    def __init__(self):

#    def __del__(self):
#        self.con.close()

    def Initialize(self):
        sql = u"""
create table IF NOT EXISTS db_log (
    id INTEGER PRIMARY KEY AUTOINCREMENT
    , screen_name varchar(20)
    , timestamp TIMESTAMP DEFAULT (DATETIME('now', 'localtime'))
);
"""
        c = self.con.cursor()
        c.execute(sql)
        self.con.commit()
        c.close()

    def Reset(self):
        sql = u"DROP TABLE db_log;"
        c = self.con.cursor()
        c.execute(sql)
        self.Initialize()
        c.close()

    def InsertLog(self, sn):
        sql = u"insert into db_log (screen_name) values (?)"
        c = self.con.cursor()
        c.execute(sql, (sn,))
        self.con.commit()
        c.close()

    def SelectLog(self):
        sql = u"select * from db_log"
        c = self.con.cursor()
        res = c.execute(sql)
        return res

    def get_active_user(self):
        MINUTE = 5
        sql = u"select * from db_log where `timestamp` > datetime('now', 'localtime', '-" + str(MINUTE) + " minute')"
        c = self.con.cursor()
        stmt = c.execute(sql)
        return stmt

    def get_active_user_wrap(self):
        stmt = self.get_active_user()
#        print(stmt.fetchall())
        return [{"name": r[1], "last_accress": r[2]} for r in stmt.fetchall()]

#    def SelectLog(self): 
if __name__ == '__main__':
    lm = LogModel()
    lm.InsertLog('fuga!')
    res = lm.get_active_user_wrap()
    print (res)
