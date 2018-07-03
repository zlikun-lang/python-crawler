# coding:utf-8
# author:zlikun

import pymysql

# 连接数据库，返回连接对象
from pymysql import DatabaseError

conn = pymysql.connect(host='192.168.0.200',
                       user='root',
                       password='123456',
                       db='user',
                       charset='utf8',
                       cursorclass=pymysql.cursors.DictCursor)

try:
    # 创建游标对象，使用with语句，自动关闭连接
    with conn.cursor() as cursor:
        # 查询SQL
        sql = 'select version()'
        # 执行查询
        cursor.execute(sql)
        # 获取查询结果(一条记录)
        result = cursor.fetchone()
        # 打印结果
        # {'version()': '8.0.11'}
        print(result)

    # 插入数据
    with conn.cursor() as cursor:
        sql = "insert into user (nickname, mobile, password, ctime) values (%s, %s, md5(%s), now())"

        try:
            cursor.execute(sql, ('Peter', '12100000002', '123456'))
            # 需要提交事务
            # connection is not autocommit by default. So you must commit to save your changes.
            conn.commit()
        except DatabaseError as e:
            conn.rollback()

    # 查询数据
    with conn.cursor() as cursor:
        sql = "select * from user limit 10"
        cursor.execute(sql)
        for r in cursor.fetchall():
            print(r)

    # 更新数据
    with conn.cursor() as cursor:
        # 数字类型的占位符也要使用`%s`，即：字符串
        sql = "update user set status = %s where mobile = %s"
        cursor.execute(sql, (1, '12100000002'))
        conn.commit()

    # 删除数据
    with conn.cursor() as cursor:
        sql = "delete from user where mobile = %s"
        cursor.execute(sql, ('12100000001',))
        # 仅用于测试，所以这里回滚
        conn.rollback()

finally:
    conn.close()