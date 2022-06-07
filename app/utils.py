from app.app import db
from app.config import Config
from datetime import datetime


class Inventory(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(80), nullable=False)
      description = db.Column(db.String(80), nullable=True)
      price = db.Column(db.Integer, nullable=False)
      quantity = db.Column(db.Integer, default=1)
      date_created = db.Column(db.DateTime, default=datetime.utcnow)
  
      def __repr__(self):
          return '<Inventory %r>' % self.name

class DeletedInventory(db.Model):
      id = db.Column(db.Integer, primary_key=True)
      name = db.Column(db.String(80), nullable=False)
      description = db.Column(db.String(80), nullable=True)
      price = db.Column(db.Integer, nullable=False)
      quantity = db.Column(db.Integer, default=1)
      date_created = db.Column(db.DateTime, default=datetime.utcnow)
      reason_for_deletion = db.Column(db.String(80), nullable=False)
  
      def __repr__(self):
          return '<Inventory %r>' % self.name