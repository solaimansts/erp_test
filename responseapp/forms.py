from django import forms

from responseapp.models import orfForm


class MyForm(forms.ModelForm):
    class Meta:
        model = orfForm
        fields = ['field_names',
                  'customer_name',
                  'customer_address',
                  'site_address',
                  'orf_no',
                  'date',
                  'work_order_no',
                  'work_order_date',
                  'quotation_ref_no',
                  'quotation_date',
                  'project_title',
                  'job_details',
                  'project_order_value',
                  'payment_terms',
                  'job_duration',
                  'job_starting_date',
                  'job_completion_date',
                  'expected_precom_date',
                  'expected_com_date',
                  'handover_date_exp',
                  'handover_date_act',
                  'name_of_project_incharge',
                  'name_of_site_incharge',
                  'advance_payment',
                  'particulars',
                  'budgeted_amount',
                  'actual_amount',
                  'variance',
                  'remarks',
                  'notes',
                  'total_cost',
                  'amount_to_be_paid_cash',
                  'amount_to_be_paid_cheque']
