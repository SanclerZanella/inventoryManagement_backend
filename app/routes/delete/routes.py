from flask import (Blueprint, render_template,
                   url_for, request, redirect, flash)
from app.app import db
from app.utils import Inventory, DeletedInventory


# Flask Blueprint
delete_item = Blueprint("delete", __name__)

@delete_item.route('/delete_item/<int:id>', methods=["GET", "POST"])
def delete(id):
