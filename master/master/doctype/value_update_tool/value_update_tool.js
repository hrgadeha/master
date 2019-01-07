// Copyright (c) 2019, frappe and contributors
// For license information, please see license.txt

frappe.ui.form.on('Value Update Tool', {
	refresh: function(frm) {

	}
});

frappe.ui.form.on("Value Update Tool", "onload", function(frm) {
    cur_frm.set_query("name1", function() {
        return {
            "filters": {
                "docstatus": 1
            }
        };
    });
});

frappe.ui.form.on("Value Update Tool", {
    "get_data": function(frm) {
		var temp1 = String(frm.doc.doctype)
        	frappe.model.with_doc(temp1, frm.doc.name1, function() {
		cur_frm.clear_table("value_update_tool_table");
            		var tabletransfer= frappe.model.get_doc(temp1, frm.doc.name1)
            		$.each(tabletransfer.items, function(index, row){
                		var d = frm.add_child("value_update_tool_table");
				d.item_name = row.item_code;
				d.description = row.description;
				d.qty = row.qty;
				d.rate = row.rate;
				d.amount = row.amount;
                	frm.refresh_field("value_update_tool_table");
            });
        });
}
});

frappe.ui.form.on("Value Update Tool", "on_submit", function(frm, doctype, name) {
frappe.call({
	"method": "master.master.doctype.value_update_tool.update_value",
	args: {
		doctype: frm.doc.doctype,
		name: frm.doc.name1,
		company: frm.doc.company
     	},

	callback:function(r){
     ;}
});
});
