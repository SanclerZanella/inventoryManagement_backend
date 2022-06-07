from flask import (Blueprint, render_template,
                   url_for, request, redirect, flash)
from app.app import db
from app.utils import Inventory, DeletedInventory


# Flask Blueprint
update_item = Blueprint("update", __name__)

@update_item.route('/update_item/<int:id>', methods=["GET", "POST"])
def update(id):
  return redirect('/')