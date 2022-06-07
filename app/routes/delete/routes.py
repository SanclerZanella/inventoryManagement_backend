from flask import (Blueprint, render_template,
                   url_for, request, redirect, flash)
from app.app import db
from app.utils import Inventory, DeletedInventory


# Flask Blueprint
delete_item = Blueprint("delete", __name__)

@delete_item.route('/delete_item/<int:id>', methods=["GET", "POST"])
def delete(id):
  product_to_delete = DeletedInventory.query.get_or_404(id)

  try:
        db.session.delete(product_to_delete)
        db.session.commit()
        flash('Item permanently deleted!')
        return redirect('/')
  except:
        flash('There was a problem deleting that product')
        return redirect('/')
