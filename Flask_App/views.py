from flask import render_template,request,redirect,url_for,flash
from Flask_App import app,db
from Flask_App.models import Table
app.secret_key="secret key"
@app.route("/")
@app.route("/home")
def home():
    data=Table.query.filter_by().all()
    return render_template("index.html",data=data)

@app.route("/insert",methods=['POST'])
def  insert():
    if request.method=='POST':
        flash("Data Inserted Successfully")
        name = request.form['name']
        phone = request.form['phone']
        color = request.form['color']
        # Table.Name=name
        # Table.Phone=phone
        # Table.Color=color
        t=Table(Name=name,Phone=phone,Color=color)
        db.session.add(t)
        db.session.commit()
        return redirect(url_for('home'))
    data = Table.query.filter_by().all()
    return render_template("index.html",data=data)

@app.route("/update/<int:ids>",methods=['POST','GET'])
def update(ids):
    if request.method=='POST':
        flash("Data Updated Successfully")
        #id=request.form['id'] another way of doing-> uncomment this and remove 'ids'
        name = request.form['name']
        phone = request.form['phone']
        color = request.form['color']
        t=Table.query.filter_by(ID=ids).first()
        t.Name=name
        t.Phone=phone
        t.Color=color
        db.session.commit()
        return redirect(url_for('home'))
    data = Table.query.filter_by().all()
    return render_template("index.html", data=data)

@app.route("/delete/<int:ids>",methods=['POST','GET'])
def delete(ids):
    t = Table.query.get_or_404(ids)
    db.session.delete(t)
    db.session.commit()
    flash("Data Deleted Successfully")
    return redirect(url_for('home'))







