from flask import (Blueprint, render_template,
                   url_for, request, redirect, flash)
from app.app import db
from app.utils import Inventory, DeletedInventory


# Flask Blueprint
update_item = Blueprint("update", __name__)

@update_item.route('/update_item/<int:id>', methods=["GET", "POST"])
def update(id):
  product = Inventory.query.get_or_404(id)

  if request.method == 'POST':
      product.name = request.form['productName']
      product.description = request.form['productDesc']
      product.price = request.form['productPrice']
      product.quantity = request.form['productQty']

      try:
          db.session.commit()
          flash('Item Successfully Updated')
          return redirect('/')
      except:
          flash('There was an issue updating your product')
          return redirect('/')

  else:
    return redirect('/')