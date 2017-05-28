#Author Qili Sui
#AdminPage Project at RBtrader
#Current Status: Development Stage - Jan 31st 2017

import pymysql.cursors
from flask import Flask, render_template,request,json

app = Flask(__name__)

#Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='root',
                             db='rbuser',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)


try:
    #with connection.cursor() as cursor:
        #Create a new record
        #sql = "INSERT INTO `users`(user_id,fname,lname,email,uname,pw) VALUES (%s, %s, %s, %s, %s, %s)"
        #cursor.execute(sql, ('7832943','Jane','DA','111Jane000@qq.com','jane0002','Janepasscode'))

    #connection is not autocommit by default. So you must commit to save
    #your changes.
    #connection.commit()

    # with connection.cursor() as cursor:
        #Read a single record
        #sql = "SELECT `user_id`, `pw` FROM `users` WHERE `email` = %s"
        #cursor.execute(sql, ('qili.rb.intern@gmail.com'))
        # sql_usersTABLE_all = "SELECT `*` FROM `users`"
        # table_name = 'User'
        # cursor.execute(sql_usersTABLE_all)
        # result_of_userTABLE = cursor.fetchall()
        #result = cursor.fetchone()
        #print(result)
        #print (type(result))
        #print(result_of_userTABLE)
        #print(type(result_of_userTABLE))

    with connection.cursor() as cursor:
        sql_joinTest = "SELECT `user_id`,`lname`,`uname`,`email`,`linker`,`tradeCipher`,`spreadViewer`,`volGraph`,`liveCurve` FROM `app` INNER JOIN `users` ON `idUser`= `user_id`"
        join_name = 'Join Result of Users Table & App Table'
        cursor.execute(sql_joinTest)
        result_of_joinTest = cursor.fetchall()
        print(result_of_joinTest)

finally:
    connection.close()

@app.route('/')
def demo():
    return render_template('data_display.html', lis = result_of_joinTest, tname = join_name )

if __name__ == "__main__":
    app.run()
