from flask import (Blueprint, render_template,
                   url_for, request, redirect, flash)
from app.app import db
from app.utils import Inventory, DeletedInventory

# Flask Blueprint
remove_item = Blueprint("remove", __name__)

@remove_item.route('/remove_item/<int:id>', methods=["GET", "POST"])
def bin(id):
  return redirect('/')