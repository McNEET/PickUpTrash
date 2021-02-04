# -*- coding:utf-8 -*-
# @Time : 2021/1/25 18:02
# @Author : liu_w
# @File : data_save
# @Function : 业务说明

import sqlite3


class MySqlUtils(object):
    def __init__(self) -> None:
        super().__init__()
        self.conn = sqlite3.connect('xianyu.db')
        print("Opened database successfully")
        self.c = self.conn.cursor()

    def create_table(self):
        """
        创建表 只调用一次
        :return:
        """
        self.c.execute('''CREATE TABLE XIANYU_GOODS
               (ID INTEGER PRIMARY KEY   AUTOINCREMENT  NOT NULL,
               NAME           TEXT    NOT NULL,
               PRICE            FLOAT     NOT NULL,
               ADDRESS        CHAR(50),
               DESCRIBE       CHAR(150),
               OTHER         CHAR(100));''')
        print("Table created successfully")
        self.conn.commit()

    def insert_data(self,name,price,address,describe,other):
        sql_ = f"INSERT INTO XIANYU_GOODS (NAME,PRICE,ADDRESS,DESCRIBE,OTHER) VALUES ({name}, {price}, {address}, {describe},{other})"
        self.c.execute(sql_)
        self.conn.commit()
        print("Insert data successfully")


if __name__ == '__main__':
    #MySqlUtils().create_table()
    MySqlUtils().insert_data("'name'",33.0,"'address'","'describe'","'other'")
