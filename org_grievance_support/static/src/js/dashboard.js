/** @odoo-module */
import { registry} from '@web/core/registry';
import { useService } from "@web/core/utils/hooks";
const { Component, onWillStart, onMounted} = owl
import { jsonrpc } from "@web/core/network/rpc_service";
import { _t } from "@web/core/l10n/translation";

export class GrievanceDashboard extends Component {
    setup() {
        this.action = useService("action");
        this.orm = useService("orm");
        this.rpc = this.env.services.rpc
        onWillStart(this.onWillStart);
        onMounted(async () => {
            this.render_project_task();
            this.render_top_employees_graph();
        });
    }
    async onWillStart() {
        await this.fetch_data();
    }
    fetch_data() {
        var self = this;
        var dataresult = jsonrpc('/grievance/datacount')
            .then(function(result) {
                self.pending_count = result['pending_count'];
                self.ongoing_count = result['ongoing_count'];
                self.resolved_count = result['resolved_count'];
        });
        return $.when(dataresult);
    }
    viewPending(e) {
        e.stopPropagation();
        e.preventDefault();
        this.action.doAction({
            name: _t("Employee Grievance"),
            type: 'ir.actions.act_window',
            res_model: 'employee.grievance',
            domain: [
                ["status", "=", 'pending']
            ],
            view_mode: 'list,form',
            views: [
                [false, 'list'],
                [false, 'form']
            ],
            target: 'current'
        })
    }
    viewOnGoing(e) {
        e.stopPropagation();
        e.preventDefault();
        this.action.doAction({
            name: _t("Employee Grievance"),
            type: 'ir.actions.act_window',
            res_model: 'employee.grievance',
            domain: [
                ["status", "=", 'on_going']
            ],
            view_mode: 'list,form',
            views: [
                [false, 'list'],
                [false, 'form']
            ],
            target: 'current'
        })
    }
    viewResolved(e) {
        e.stopPropagation();
        e.preventDefault();
        this.action.doAction({
            name: _t("Employee Grievance"),
            type: 'ir.actions.act_window',
            res_model: 'employee.grievance',
            domain: [
                ["status", "=", 'resolved']
            ],
            view_mode: 'list,form',
            views: [
                [false, 'list'],
                [false, 'form']
            ],
            target: 'current'
        })
    }
    async render_project_task() {
        await jsonrpc("/grievance/count").then(function(data) {
            var ctx = $("#grievance_doughnut");
            new Chart(ctx, {
                type: "doughnut",
                data: {
                    labels: data.grievance,
                    datasets: [{
                        backgroundColor: data.color,
                        data: data.total
                    }]
                },
                options: {
                    legend: {
                        position: 'left'
                    },
                    cutoutPercentage: 40,
                    responsive: true,
                }
            });
        })
    }
    async render_top_employees_graph() {
        var ctx = $("#grievance_bar");
        await jsonrpc('/grievance/bar').then(function(arrays) {
            var data = {
                labels: arrays[1],
                datasets: [{
                        label: "Hours Spent",
                        data: arrays[0],
                        backgroundColor: [
                            "rgba(190, 27, 75,1)",
                            "rgba(31, 241, 91,1)",
                            "rgba(103, 23, 252,1)",
                            "rgba(158, 106, 198,1)",
                            "rgba(250, 217, 105,1)",
                            "rgba(255, 98, 31,1)",
                            "rgba(255, 31, 188,1)",
                            "rgba(75, 192, 192,1)",
                            "rgba(153, 102, 255,1)",
                            "rgba(10,20,30,1)"
                        ],
                        borderColor: [
                            "rgba(190, 27, 75, 0.2)",
                            "rgba(190, 223, 122, 0.2)",
                            "rgba(103, 23, 252, 0.2)",
                            "rgba(158, 106, 198, 0.2)",
                            "rgba(250, 217, 105, 0.2)",
                            "rgba(255, 98, 31, 0.2)",
                            "rgba(255, 31, 188, 0.2)",
                            "rgba(75, 192, 192, 0.2)",
                            "rgba(153, 102, 255, 0.2)",
                            "rgba(10,20,30,0.3)"
                        ],
                        borderWidth: 1
                    },

                ]
            };
            //options
            var options = {
                responsive: true,
                title: {
                    display: true,
                    position: "top",
                    text: " Status",
                    fontSize: 18,
                    fontColor: "#111"
                },
                legend: {
                    display: false,
                },
                scales: {
                    yAxes: [{
                        ticks: {
                            min: 0
                        }
                    }]
                }
            };
            //create Chart class object
            var chart = new Chart(ctx, {
                type: 'bar',
                data: data,
                options: options
            });

        });
    }

}
GrievanceDashboard.template = "GrievanceDashboard"
registry.category("actions").add("grievance_dashboard", GrievanceDashboard)
