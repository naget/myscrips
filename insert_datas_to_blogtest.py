import datetime

import pymysql

def do():
    conn = pymysql.connect(host='127.0.0.1', user="root", passwd="password", port=3306, charset="utf8")
    cur = conn.cursor()

    group_sql = "insert into blogtest.groups(name) value (%s)"
    user_sql = "insert into blogtest.users(name,sex,group_id) value(%s,%s,%s) "
    article_sql = "insert into blogtest.article(title,content,summary,author_id) value(%s,%s,%s,%s) "
    category_sql = "insert into blogtest.category(article_id,type) value(%s,%s)"
    liked_sql = "insert into blogtest.like_record(article_id,liker_id) value (%s,%s)"
    group = ["web后端", "web前端", "安卓", "嵌入式"]
    base = 0
    try:
        for i in range(4):
            print("i=", i)
            groupname = group[i]
            cur.execute(group_sql, groupname)
            for j in range(10000):
                user_param = ["wang"+str(base+j), 0, i+1]
                cur.execute(user_sql, user_param)
            base = base+10000
        for w in range(1000000):
            article_param = ["title"+str(w), "content"+str(w), "summary"+str(w), w % 40000+1]
            cur.execute(article_sql, article_param)
            category_param = [w+1, "type"+str(w % 6)]
            cur.execute(category_sql, category_param)
            liked_param = [w+1, (w+15869) % 39999]
            cur.execute(liked_sql, liked_param)
    except Exception as e:
        print("出问题了", e.with_traceback(e))
        cur.close()
        conn.rollback()
    conn.commit()
    conn.close()


if __name__ == "__main__":
    start = datetime.datetime.now()
    do()
    end = datetime.datetime.now()
    print("插入三百多万条数据耗时", (end-start).seconds ,"秒")