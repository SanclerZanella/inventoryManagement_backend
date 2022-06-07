from flask import (Blueprint, render_template,
                   url_for, request, redirect, flash)
from app.app import db
from app.utils import Inventory, DeletedInventory

# Flask Blueprint
index_page = Blueprint("index", __name__)

@index_page.route('/', methods=["GET", "POST"])
def index():
    """
    View to render the index page
    """
    if request.method == "POST":
      name = request.form['productName']
      description = request.form['productDesc']
      price = request.form['productPrice']
      quantity = request.form['productQty']
      new_product = Inventory(name=name, description=description, price=price, quantity=quantity)

      try:
              db.session.add(new_product)
              db.session.commit()
              flash("Item Successfuly Added")
              return redirect('/')
      except Exception as e:
          return f"{e}"

    else:
        products = Inventory.query.order_by(Inventory.date_created).all()
        deleted_products = DeletedInventory.query.order_by(DeletedInventory.date_created).all()
        return render_template("index.html", products=products, deleted_products=deleted_products)
