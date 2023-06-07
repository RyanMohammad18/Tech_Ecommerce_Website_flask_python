from bson import ObjectId
from flask import Flask, render_template, request, flash, url_for, session, redirect

from shop import app, db, test_collection, test_collection2,test_collection_3,test_collection_4

import os


picfolder = os.path.join('static', 'images')
app.config['UPLOAD_FOLDER'] = picfolder
@app.route('/')
def home1():
    return render_template("index.html",**locals())
@app.route('/home')
def home():
    pic1= os.path.join(app.config['UPLOAD_FOLDER'],'4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')

    return render_template("index.html",**locals())
@app.route('/userhome')
def userhome():
    pic1= os.path.join(app.config['UPLOAD_FOLDER'],'4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')


    return render_template("index2.html",**locals())

@app.route('/aboutus')
def aboutus():
    pic1= os.path.join(app.config['UPLOAD_FOLDER'],'4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')

    return render_template("aboutus.html",**locals())

@app.route('/mobile')
def mobile_categories():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')
    return render_template("index2.html",**locals())

@app.route('/computer')
def computer_categories():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')
    return render_template("computer.html",**locals())

@app.route('/headphone')
def headphone_categories():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')
    return render_template("headphone.html",**locals())


@app.route("/registration",methods=['GET','POST'])
def registration():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')


    post=False
    if request.method=='POST':
        post=True
        username=request.form['username']
        password=request.form['password']
        cpassword=request.form['cpassword']
        error=""
        if password != cpassword:
            error="Password didn't match"
        elif password==cpassword:
            result = test_collection.find_one({"username": username})
            if result is not None:
                error="User already exists."
            else:
                test_collection.insert_one(dict(request.form))
                error=username+" added successfully,Go to login page"
    return render_template("registration.html",**locals())


@app.route("/login",methods=["GET","POST"])
def login():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')


    post = False
    if request.method == 'POST':
        post = True
        username = request.form['username']
        password = request.form['password']
        error = ""
        result = test_collection.find_one({"username": username})
        result2=test_collection.find_one({"password":password})
        admin='raiyan@gmail.com'
        adminpassword='raiyankohli18'
        if result is None:
            error = "Password Did not match"
        if username==admin and password==adminpassword:
            return redirect('/home')
        if username==result and password==result2:
            return redirect('/userhome')
        else:
            error  = "Login Successfully"
    return  render_template("login.html",**locals())



@app.route('/addcategories', methods=['GET', "POST"])
def addcategories():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')


    is_post = False
    categories_post = False
    if request.method == "POST":
        is_post = True
        form_data = request.form
        categories = form_data["categories"]

        newCategories = {
            "categories": categories,
        }
        print(newCategories)
        if categories is not None:
            test_collection2.insert_one(newCategories)
            categories_post = True
            return redirect("/categories")

    return render_template("addcategories.html", **locals())


@app.route("/categories",methods=["GET","POST"])
def categories():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')
    if request.method=='POST':
        categories = []
        name=request.form['categories']
        for data in test_collection2.find({"categories":name}):
            print(data)
            categories.append(data)
    else:
        categories = []
        for data in test_collection2.find():
            print(data)

            categories.append(data)
    return render_template("categories.html", **locals())

@app.route("/updatecategories/<string:id>", methods=['GET', "POST"])

def updatecategories(id):
    single_categories = test_collection2.find_one({"_id": ObjectId(id)})
    print(single_categories)
    if request.method == "POST":
        form_data = request.form
        categories = form_data["categories"]
        updatedcategories = {'categories': categories}
        filter = {'categories': single_categories['categories']}
        newvalues = { "$set": {updatedcategories} }
        test_collection2.update_one(filter, newvalues)
        return redirect("/categories")
    test_collection2.delete_one({"_id": ObjectId(id)})
    return render_template("updatecategories.html", **locals())



@app.route("/delete/<string:categories>", methods=['GET', "POST"])
def delete(categories):
    if (test_collection2.delete_one({"categories": categories})):
        return "deleted"
    return render_template("delete.html",**locals())

@app.route("/cart", methods=['GET', "POST"])
def cart():
    if request.method == "POST":
        is_post = True
        form_data = request.form
        categories = form_data["categories"]

        newCategories = {
            "categories": categories,
        }
        print(newCategories)
        if categories is not None:
            test_collection_3.insert_one(newCategories)
            categories_post = True
            return redirect("/cart")

    return render_template("cart.html", **locals())
    
@app.route('/addProduct', methods=['GET', "POST"])
def addProduct():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')


    is_post = False
    categories_post = False
    if request.method == "POST":
        is_post = True
        form_data = request.form
        categories = form_data["categories"]
        price = form_data["price"]

        newCategories = {
            "categories": categories,
            "price": price,
        }
        print(newCategories)
        if categories is not None:
            test_collection_3.insert_one(newCategories)
            categories_post = True
            return redirect("/product")

    return render_template("addProduct.html", **locals())


@app.route("/product",methods=["GET","POST"])
def product():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')
    if request.method=='POST':
        categories = []
        name=request.form['categories']
        for data in test_collection_3.find({"categories":name}):
            print(data)
            categories.append(data)
    else:
        categories = []
        for data in test_collection_3.find():
            print(data)

            categories.append(data)
    return render_template("product.html", **locals())
@app.route("/userproduct",methods=["GET","POST"])
def userproduct():
    pic1 = os.path.join(app.config['UPLOAD_FOLDER'], '4.jpg')
    pic2 = os.path.join(app.config['UPLOAD_FOLDER'], '5.jpg')
    pic3 = os.path.join(app.config['UPLOAD_FOLDER'], '6.jpg')
    pic4 = os.path.join(app.config['UPLOAD_FOLDER'], '7.jpg')
    if request.method=='POST':
        categories = []
        name=request.form['categories']
        for data in test_collection_3.find({"categories":name}):
            print(data)
            categories.append(data)
    else:
        categories = []
        for data in test_collection_3.find():
            print(data)

            categories.append(data)
    return render_template("userproduct.html", **locals())

@app.route("/addorder",methods=['GET','POST'])
def addorder():
    text='Thanks for your order'
    is_post = False
    categories_post = False
    if request.method == "POST":
        is_post = True
        form_data = request.form
        name = form_data["name"]
        address = form_data["address"]
        phone = form_data["phone"]
        district = form_data["district"]
        i=1;
        newCategories = {
            "name": name,
            "address":address,
            "phone":phone,
            "district":district,
        }
        print(newCategories)
        if name is not None:
            i=i+1
            test_collection_4.insert_one(newCategories)

            categories_post = True
            return text

    return render_template("addorder.html",**locals())

@app.route("/order",methods=['GET','POST'])
def order():

    if request.method=='POST':
        orderlist = []
        name=request.form['name']
        phone = request.form['phone']
        address=request.form['address']
        district = request.form['district']
        i=0
        for data in test_collection_4.find({"name":name,"phone":phone,"address":address,"district":district}):
            i=i+1
            print(data)
            orderlist.append(data)
    else:
        orderlist = []
        for data in test_collection_4.find():
            print(data)

            orderlist.append(data)
    return render_template("order.html", **locals())



@app.route("/updateproduct/<string:id>", methods=['GET', "POST"])

def updateproduct(id):
    single_product = test_collection_3.find_one({"_id": ObjectId(id)})
    print(single_product)
    if request.method == "POST":
        form_data = request.form
        name = form_data["categories"]
        price=form_data["price"]
        updatedproduct = {'categories': name,'price':price}
        filter = {'categories': single_product['categories']}
        newvalues = { "$set": {updatedproduct} }
        test_collection_3.update_one(filter, newvalues)
        return redirect("/product")
    test_collection_3.delete_one({"_id": ObjectId(id)})
    return render_template("updateproduct.html", **locals())


@app.route("/deleteproduct/<string:name>", methods=['GET', "POST"])
def deleteproduct(name):
    if (test_collection_3.delete_one({"categories": name})):
        return redirect('/product')
    return render_template("deleteproduct.html",**locals())