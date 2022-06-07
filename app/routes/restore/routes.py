from flask import (Blueprint, render_template,
                   url_for, request, redirect, flash)
from app.app import db
from app.utils import Inventory, DeletedInventory


# Flask Blueprint
restore_item = Blueprint("restore", __name__)

@restore_item.route('/restore_item/<int:id>', methods=["GET", "POST"])
def restore(id):
  product_to_restore = DeletedInventory.query.get_or_404(id)
  restored_product = Inventory(name=product_to_restore.name, description=product_to_restore.description, price=product_to_restore.price, quantity=product_to_restore.quantity)

  try:
      db.session.add(restored_product)
      db.session.commit()
      db.session.delete(product_to_restore)
      db.session.commit()
      flash('Item Successfully Restores to Inventory')
      return redirect('/')
  except:
      flash('There was an issue restoring this item')
      return redirect('/')
