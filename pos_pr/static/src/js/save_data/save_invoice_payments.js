odoo.define("pos_pr.save_invoice_payments", function (require) {

    const models = require("point_of_sale.models");
    const PosDB = require("point_of_sale.DB");
    const rpc = require('web.rpc');

    const core = require("web.core");
    const _t = core._t;

    models.PosModel = models.PosModel.extend({
        init: function (options) {
            this._super(options);
            this.pending_invoice_payments = [];
            this.pending_surcharge_invoices = [];
        },
        send_surcharge: function (surcharge) {
            if (surcharge) {
                let self = this;
                let surcharge_invoice_json = surcharge.export_as_JSON();

                surcharge_invoice_json.payment_ids = surcharge.payment_ids.map((payment) => [0, 0, payment.export_as_JSON()]);

                rpc.query({
                    model: "pos_pr.invoice.surcharge",
                    method: "create",
                    args: [surcharge_invoice_json]
                }, {}).then(function (surcharge_invoice_id) {
                    self.gui.show_popup('confirm', {
                        'title': _t('Surcharges have been created'),
                        'body': _t('The Surcharges have been validated, please, close the session to get these surcharges be applied to the invoices'),
                    });
                    console.log(surcharge_invoice_id);
                }).catch(function (error) {
                    if (!self.pending_surcharge_invoices) {
                        self.pending_surcharge_invoices = [];
                    }
                    self.pending_surcharge_invoices.push(surcharge_invoice_json);
                    console.error(error);
                });
            }

        },

        send_invoice_payments: function (invoicePayments) {
            let self = this;
            return new Promise(function (resolve, reject) {
                if (invoicePayments) {
                    let invoicePaymentsJson = invoicePayments.map((payment) => payment.export_as_JSON());
                    rpc.query({
                        model: "pos_pr.invoice.payment",
                        method: "create",
                        args: [invoicePaymentsJson]
                    }).then(function (invoicePaymentIds) {
                        self.gui.show_popup('confirm', {
                            'title': _t('Payments have been validated'),
                            'body': _t('The payments have been validated, please, close the session to get these payments be applied to the invoices'),
                        });
                        resolve();
                    }).catch(function (error) {
                        if (!self.pending_invoice_payments) {
                            self.pending_invoice_payments = [];
                        }
                        self.pending_invoice_payments.push(...invoicePaymentsJson);
                        console.error(error);
                        reject();
                    });
                }
            });
        }
    });

});
