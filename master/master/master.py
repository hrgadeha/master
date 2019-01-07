@frappe.whitelist()
def update_poitem(poitem, qty, rate, expected_delivery_date,
				  schedule_date, partial_update_notes):
	poitem = frappe.get_doc('Purchase Order Item', poitem)
	for field in poitem.meta.fields:
		if field.fieldname:
			poi_field = poitem.meta.get_field(field.fieldname)
			if poi_field:
				poi_field.allow_on_submit = True
	poitem.qty = float(qty)
	poitem.rate = float(rate)
	poitem.expected_delivery_date = expected_delivery_date
	poitem.schedule_date = schedule_date
	poitem.partial_update_notes = partial_update_notes
	poitem.save()
	poitem.reload()
	return {
		'poitem': poitem
	}


@frappe.whitelist()
def update_po(po):
	po = frappe.get_doc('Purchase Order', po)
	for field in po.meta.fields:
		if field.fieldname:
			po_field = po.meta.get_field(field.fieldname)
			if po_field:
				po_field.allow_on_submit = True
	po.save()
	po.reload()
	return {
		'po': po
	}
