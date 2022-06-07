from flask import (Blueprint, render_template,
                   url_for, request, redirect, flash)
from app.app import db
from app.utils import Inventory, DeletedInventory


# Flask Blueprint
remove_item = Blueprint("remove", __name__)

@remove_item.route('/remove_item/<int:id>', methods=["GET", "POST"])
def bin(id):
   if request.method == 'POST':
       product_to_delete = Inventory.query.get_or_404(id)
       deleted_inventory = DeletedInventory(name=product_to_delete.name, description=product_to_delete.description, price=product_to_delete.price, quantity=product_to_delete.quantity, reason_for_deletion=request.form['deleteReason'])

       try:
           db.session.add(deleted_inventory)
           db.session.commit()
           db.session.delete(product_to_delete)
           db.session.commit()
           flash("Item Successfuly Moved to the Bin")
           return redirect('/')
       except:
           flash("There was an issue moving this product to the bin")
           return redirect('/')
   else:
     return redirect('/')
     