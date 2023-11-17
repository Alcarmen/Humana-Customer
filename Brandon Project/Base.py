from flask import Flask, render_template,request,url_for,redirect
from dbhelper import *

app = Flask(__name__)
#app.config['SECRET KEY']= '696969BRANDON696969'

@app.route('/')
def home():
    return render_template("Home.html")
    
@app.route('/Custom',methods=['GET','POST'])
def Custom():
    data = getall("customers")
    head:list= ['C_id','C_name','c_email','c_address', 'actions']       
      
    return render_template("index.html", student=data, header=head)
    
@app.route('/Item')
def Item():
    it= getall("items")
    head:list= ['id','ISBN','Title','Author','Genre', 'Price','I_Type', 'Action']
    return render_template("itemindex.html",item=it, header=head)
 
@app.route('/create', methods=['GET','POST'])
def create():
    if request.method == 'POST':
        c_name,c_email,c_address=dict(request.form).values()
        addrecord('customers',c_name=c_name, c_email=c_email, c_address=c_address)
        return redirect(url_for('Custom'))
    return render_template("Create.html")

@app.route('/update/<c_id>', methods=['GET','POST'])
def update(c_id):
    if request.method == 'POST':
        c_name,c_email,c_address=dict(request.form).values()
        updaterecord('customers',c_id=c_id,c_name=c_name, c_email=c_email, c_address=c_address)
        return redirect(url_for('Custom'))
       
    return render_template("Update.html")
        
@app.route('/delete_cust/<c_id>',methods=['GET'])
def delete_cust(c_id):
    if request.method == 'GET':
        deleterecord('customers',c_id=c_id)
        return redirect(url_for("Custom"))
        
@app.route('/search', methods=['GET', 'POST'])
def search():
    if request.method == 'POST':
        search_query = request.form.get('search_query')
        print("Search Query:", search_query)  # Check if the query is captured correctly

        results = searchrecord('customers', search_query)
        print("Results:", results)  # Check the results obtained

        if not results:
            # Implement an appropriate message or action when no results are found
            return render_template("NoResults.html")  # Create a NoResults.html template

        return render_template("Searched.html", results=results)

    return redirect(url_for("Custom"))


        
if __name__=='__main__':
    
    app.run(debug=True)