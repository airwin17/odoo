import { registry } from "@web/core/registry";
import { ControlPanel } from "@web/search/control_panel/control_panel";
import { Component } from "@odoo/owl";

/** 
 * Odoo Control Panel Extension Example
 * File: control_panel.js
 */


export class SparepartControlPanel extends Component {}

SparepartControlPanel.template = "sparepart.ControlPanel";

// Register the new control panel (example usage)
registry.category("control_panel").add("sparepart_control_panel", {
    component: SparepartControlPanel,
});