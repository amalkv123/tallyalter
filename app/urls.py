from django.urls import path,include
from.import views


urlpatterns = [

    path('',views.base,name='base'),
    path('changecompany',views.changecompany,name='changecompany'),
    path('createcompony',views.createcompony,name='createcompony'),
    path('crtecompony',views.crtecompony,name='crtecompony'),
    path('selectcompony',views.selectcompony,name='selectcompony'),
    
    path('alter_payrol_emp_add2',views.alter_payrol_emp_add2,name='alter_payrol_emp_add2'),
    
    path('alter_payrol_employee',views.alter_payrol_employee,name='alter_payrol_employee'),
    path('alter_payrol_addemployee',views.alter_payrol_addemployee,name='alter_payrol_addemployee'),
    path('alter_payrol_payheads',views.alter_payrol_payheads,name='alter_payrol_payheads'),
    path('alter_payrol_attendence3',views.alter_payrol_attendence3,name='alter_payrol_attendence3'),
    path('alter_payrol_attendence',views.alter_payrol_attendence,name='alter_payrol_attendence'),
    path('attendence',views.attendence,name='attendence'),
    path('alter_payrol_attendence_edit/<int:pk>',views.alter_payrol_attendence_edit,name='alter_payrol_attendence_edit'),
    path('alter_payrol_attendence_edit2/<int:pk>',views.alter_payrol_attendence_edit2,name='alter_payrol_attendence_edit2'),
    
    path('alter_payrol_employee2',views.alter_payrol_employee2,name='alter_payrol_employee2'),
    path('payheads',views.payheads,name='payheads'),
    
    
    path('alter_payrol_emp_gredit/<int:pk>',views.alter_payrol_emp_gredit,name='alter_payrol_emp_gredit'),
    path('alter_payrol_emp_gredit2/<int:pk>',views.alter_payrol_emp_gredit2,name='alter_payrol_emp_gredit2'),
    path('alter_payrol_add_voucher',views.alter_payrol_add_voucher,name='alter_payrol_add_voucher'),
    path('alter_payrol_add_voucher2',views.alter_payrol_add_voucher2,name='alter_payrol_add_voucher2'),
    path('alter_payrol_add_voucher3',views.alter_payrol_add_voucher3,name='alter_payrol_add_voucher3'),
    path('alter_payrol_add_voucher_edit/<int:pk>',views.alter_payrol_add_voucher_edit,name='alter_payrol_add_voucher_edit'),
    path('alter_payrol_add_voucher_edit2/<int:pk>',views.alter_payrol_add_voucher_edit2,name='alter_payrol_add_voucher_edit2'),
    path('alter_payrol_unit',views.alter_payrol_unit,name='alter_payrol_unit'),
    path('alter_payrol_unit2',views.alter_payrol_unit2,name='alter_payrol_unit2'),
    path('unit3',views.unit3,name='unit3'),
    
    path('alter_payrol_unit_edit/<int:pk>',views.alter_payrol_unit_edit,name='alter_payrol_unit_edit'),
    path('alter_payrol_unit_edit2/<int:pk>',views.alter_payrol_unit_edit2,name='alter_payrol_unit_edit2'),
    path('alter_statutory_gst3',views.alter_statutory_gst3,name='alter_statutory_gst3'),
    path('alter_statutory_panadd',views.alter_statutory_panadd,name='alter_statutory_panadd'),
    path('alter_statutory_pan2',views.alter_statutory_pan2,name='alter_statutory_pan2'),
    path('alter_statutory_gst2',views.alter_statutory_gst2,name='alter_statutory_gst2'),
    path('add_payhead',views.add_payhead,name='add_payhead'),
    path('alter_payrol_payhead_edit/<int:pk>',views.alter_payrol_payhead_edit,name='alter_payrol_payhead_edit'),
    path('alter_payrol_payhead_edit2/<int:pk>',views.alter_payrol_payhead_edit2,name='alter_payrol_payhead_edit2'),
    path('alter_payrol_salary',views.alter_payrol_salary,name='alter_payrol_salary'),
    path('alter_payrol_salary2',views.alter_payrol_salary2,name='alter_payrol_salary2'),
    path('alter_payrol_load_calculation',views.alter_payrol_load_calculation,name='alter_payrol_load_calculation'),
    path('alter_payrol_load',views.alter_payrol_load,name='alter_payrol_load'),
    path('alter_payrol_salary3',views.alter_payrol_salary3,name='alter_payrol_salary3'),
    path('bank',views.bank,name='bank'),
    path('add_bank3',views.add_bank3,name='add_bank3'),
    path('stunits',views.stunits,name='stunits'),
    path('add_units',views.add_units,name='add_units'),
    path('uqcform',views.uqcform,name='uqcform'),
    path('stunits2',views.stunits2,name='stunits2'),
    path('emp_attendence',views.emp_attendence,name='emp_attendence'),
    path('attendence2',views.attendence2,name='attendence2'),
    path('payvoucher',views.payvoucher,name='payvoucher'),
    path('add_voucher',views.add_voucher,name='add_voucher'),
    path('emp_grp',views.emp_grp,name='emp_grp'),
    path('addemp_group',views.addemp_group,name='addemp_group'),
    path('emp_grp2',views.emp_grp2,name='emp_grp2'),
    path('employe_category_secondary',views.employe_category_secondary,name='employe_category_secondary'),
    path('employee',views.employee,name='employee'),
    path('addemployee',views.addemployee,name='addemployee'),
    path('addemp_group2',views.addemp_group2,name='addemp_group2'),
    path('salary1',views.salary1,name='salary1'),
    path('load',views.load,name='load'),
    path('load_calculation',views.load_calculation,name='load_calculation'),
    path('alter_payrol_employee_edit/<int:pk>',views.alter_payrol_employee_edit,name='alter_payrol_employee_edit'),
    #path('payvoucher',views.payvoucher,name='payvoucher'),
    #path('payvoucher',views.payvoucher,name='payvoucher'),
   






    
]