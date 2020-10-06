import pymysql as py
conn = py.connect(
    host = 'localhost',
    port = 3306,
    user = 'root',
    passwd = 'root',#数据库密码
    db = 'dh',# 数据库名
)
# 通过获取到的数据库连接conn下的cursor()方法来创建游标
cur = conn.cursor()
# 创建表
cur.execute('create table student(id int, name varchar(20), class varchar(20), age varchar(10))')

# 插入一条数据
cur.execute("insert into student values('2','gege','class 2 grade 3','20')")
cur.execute("insert into student values('2','bob','class 2 grade 5','21')")
# 修改查询条件的数据
cur.execute("update student set class = 'class 2 grade 5' where name='bob'")

# 删除查询条件的数据
cur.execute("delete from student where age='9'")
# cur.execute("drop table student3,student4,student5,student6")


cur.close()  # 关闭游标
conn.commit()  # 提交事务，向数据库插入数据时一定要加这句话，否则不会真正插入
conn.close()  #