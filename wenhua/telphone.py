from flask import Flask,render_template,redirect,url_for,request
import pymysql.cursors
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('form.html')
@app.route('/submit',methods=["POST","GET"])
def submit():
    name=request.form.get('name')
    tel=request.form.get('tel')
    connection = pymysql.connect(host='39.96.26.6', port=3306, user='root', password='zxj+15508321787', db='tel_form',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor=connection.cursor()
    sql="insert into wenhua values('%s','%s');"%(name,tel)
    try:
        cursor.execute(sql)
        connection.commit()
    except Exception:
        connection.rollback()
    return redirect(url_for('printf'))
@app.route('/printf')
def printf():
    connection2= pymysql.connect(host='39.96.26.6', port=3306, user='root', password='zxj+15508321787', db='tel_form',charset='utf8mb4', cursorclass=pymysql.cursors.DictCursor)
    cursor2=connection2.cursor()
    sql2="select * from wenhua;"
    cursor2.execute(sql2)
    u=cursor2.fetchall()
    return render_template('form_out.html',u=u)
if __name__=='__main__':
    app.run(debug=True)
