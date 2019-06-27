from django.shortcuts import render
from responseapp.forms import MyForm
from django.template import loader
from django.http import HttpResponse


def responseform(request):
    if request.method == 'POST':
        myForm = MyForm(request.POST)

        if myForm.is_valid():
            field_names = myForm.cleaned_data['field_names']
            customer_name = myForm.cleaned_data['customer_name']
            customer_address = myForm.cleaned_data['customer_address']
            site_address = myForm.cleaned_data['site_address']
            orf_no = myForm.cleaned_data['orf_no']
            date = myForm.cleaned_data['date']
            work_order_no = myForm.cleaned_data['work_order_no']
            work_order_date = myForm.cleaned_data['work_order_date']
            quotation_ref_no = myForm.cleaned_data['quotation_ref_no']
            quotation_date = myForm.cleaned_data['quotation_date']
            project_title = myForm.cleaned_data['project_title']
            job_details = myForm.cleaned_data['job_details']
            project_order_value = myForm.cleaned_data['project_order_value']
            payment_terms = myForm.cleaned_data['payment_terms']
            job_duration = myForm.cleaned_data['job_duration']
            job_starting_date = myForm.cleaned_data['job_starting_date']
            job_completion_date = myForm.cleaned_data['job_completion_date']
            expected_precom_date = myForm.cleaned_data['expected_precom_date']
            expected_com_date = myForm.cleaned_data['expected_com_date']
            handover_date_exp = myForm.cleaned_data['handover_date_exp']
            handover_date_act = myForm.cleaned_data['handover_date_act']
            name_of_project_incharge = myForm.cleaned_data['name_of_project_incharge']
            name_of_site_incharge = myForm.cleaned_data['name_of_site_incharge']
            advance_payment = myForm.cleaned_data['advance_payment']
            particulars = myForm.cleaned_data['particulars']
            budgeted_amount = myForm.cleaned_data['budgeted_amount']
            actual_amount = myForm.cleaned_data['actual_amount']
            variance = myForm.cleaned_data['variance']
            remarks = myForm.cleaned_data['remarks']
            notes = myForm.cleaned_data['notes']
            total_cost = myForm.cleaned_data['total_cost']
            amount_to_be_paid_cash = myForm.cleaned_data['amount_to_be_paid_cash']
            amount_to_be_paid_cheque = myForm.cleaned_data['amount_to_be_paid_cheque']

            context = {
                'field_names': field_names,
                'customer_name': customer_name,
                'customer_address': customer_address,
                'site_address': site_address,
                'orf_no': orf_no,
                'date': date,
                'work_order_no': work_order_no,
                'work_order_date': work_order_date,
                'quotation_ref_no': quotation_ref_no,
                'quotation_date': quotation_date,
                'project_title': project_title,
                'job_details': job_details,
                'project_order_value': project_order_value,
                'payment_terms': payment_terms,
                'job_duration': job_duration,
                'job_starting_date': job_starting_date,
                'job_completion_date': job_completion_date,
                'expected_precom_date': expected_precom_date,
                'expected_com_date': expected_com_date,
                'handover_date_exp': handover_date_exp,
                'handover_date_act': handover_date_act,
                'name_of_project_incharge': name_of_project_incharge,
                'name_of_site_incharge': name_of_site_incharge,
                'advance_payment': advance_payment,
                'particulars': particulars,
                'budgeted_amount': budgeted_amount,
                'actual_amount': actual_amount,
                'variance': variance,
                'remarks': remarks,
                'notes': notes,
                'total_cost': total_cost,
                'amount_to_be_paid_cash': amount_to_be_paid_cash,
                'amount_to_be_paid_cheque': amount_to_be_paid_cheque
            }

            template = loader.get_template('orf.html')

            return HttpResponse(template.render(context, request))



    else:
        form = MyForm()

    return render(request, 'responseform.html', {'form': form});
