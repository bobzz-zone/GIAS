# -*- coding: utf-8 -*-
# Copyright (c) 2015, Ros@gmail.com and contributors
# For license information, please see license.txt

from __future__ import unicode_literals
import frappe
from frappe.model.document import Document
from frappe import _

class PettyCash(Document):
        def before_save(self):
                amount = self.get("amount")
                posting_date = self.get("posting_date")
                pay_for = self.get("pay_for")
                received_by = self.get("received_by")


        def validate(self):
                  amount = self.get("amount")
                  posting_date = self.get("posting_date")
                  pay_for = self.get("pay_for")
                  received_by = self.get("received_by")
                  if frappe.db.get_value("Petty Cash", {"amount":amount, "posting_date":posting_date, "pay_for":pay_for, "received_by":received_by, "docstatus":1}, "name", as_dict = True):
                         frappe.throw(_("You can't create duplicate doctype"))

