from calendar import c
from multiprocessing import context
from unicodedata import name
from django.shortcuts import render,redirect
import os
from app.models import crtcompony,empgroup2,Employee,create_VoucherModels,Create_attendence,pan,create_payhead,compute_information,Rounding,gratuity,units,gst,add_bank,E_found_trasfer,create_salary,bank3,CreateEmployeeGrp,unitQuantityCode,Companies,Create_employeegroup,emp_category,P_cost_default,salary
from django.contrib.auth.models import auth,User
from django.contrib import messages


# Create your views here.

def base(request):
    return render(request, 'base.html')

def changecompany(request):
    return render(request, 'changecompany.html')

def createcompony(request):
    return render(request, 'createcompony.html')

def crtecompony(request):
    if request.method=='POST':
        comname=request.POST['componyname']
        mailingname=request.POST['mailingname']
        address=request.POST['address']
        state=request.POST['state']
        country=request.POST['country']
        pincode=request.POST['pincode']
        telphone=request.POST['telphone']
        mobile=request.POST['mobile']
        fax=request.POST['fax']
        email=request.POST['email']
        website=request.POST['website']
        fyearbgn=request.POST['fyearbgn']
        booksbgn=request.POST['booksbgn']
        curncysymbl=request.POST['curncysymbl']
        crncyname=request.POST['crncyname']
        # items=request.FILES['file']
        data=crtcompony(componyname=comname,
                    mailingname=mailingname,
                    address=address,
                    state=state,
                    country=country,
                    pincode=pincode,
                    telphone=telphone,
                    mobile=mobile,
                    fax=fax,
                    email=email,
                    website=website,
                    fyearbgn=fyearbgn,
                    booksbgn=booksbgn,
                    curncysymbl=curncysymbl,
                    crncyname=crncyname)
        data.save()
        messages.success(request,"Compony added successfully!")
        
        return redirect('/')

def selectcompony(request):
    data=crtcompony.objects.all()
    return render(request,'selectcompony.html',{'data':data})










 

def alter_statutory_pan2(request):
    return render(request,'alter_statutory_pan.html')  

def alter_payrol_attendence(request):
    data=Create_attendence.objects.all()
    return render(request,'alter_payrol_attendence2.html',{'p':data})



    #employeegroup


def emp_grp(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
        tally1 = Companies.objects.get(id=t_id)

    std=Create_employeegroup.objects.all()
    empc=emp_category.objects.all()

    return render(request,'employegroup.html',{'std':std,'empc':empc})


def addemp_group(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    empc=emp_category.objects.all()
    if request.method == 'POST':
        name= request.POST['name']
        alias = request.POST['alias']
        under = request.POST['under']
        sal= request.POST['sal']

        std= Create_employeegroup(
            name =name,
            alias=alias,
            under=under,
            define_salary=sal,   
        )
        std.save()
       # messages.success(request,'employee group add successfully !!!')
        return redirect('alter_payrol_emp_add2')
    return render(request,'employegroup.html',{'tally':tally,'empc':empc})

def emp_grp2(request):
    std=Create_employeegroup.objects.all()
    return render(request,'employegroup_secondary.html',{'std':std})

def employe_category_secondary(request):
    
    return render(request,'employe_category_secondary.html')   

def alter_payrol_emp_add2(request):
    emp=Create_employeegroup.objects.all()
    return render(request,'alter_payrol_employegroup2.html',{'data':emp})  

def alter_payrol_emp_gredit(request,pk):
    data=Create_employeegroup.objects.get(id=pk)
    data2=Create_employeegroup.objects.all()
    context={'p1':data,
    'emp':data2}
    return render(request,'alter_payrol_gredit.html',context) 

def alter_payrol_emp_gredit2(request,pk):
    if request.method=='POST':
        datas=Create_employeegroup.objects.get(id=pk)
        datas.name =request.POST.get('name')
        datas.alias = request.POST.get('alias')
        datas.under = request.POST.get('under')
        datas.define_salary = request.POST.get('sal')
        

        datas.save()
        return redirect('alter_payrol_emp_add2')




  





    #payheads



def alter_payrol_payheads(request):
    data=create_payhead.objects.all()
    return render(request,'alter_payrol_payheads2.html',{'p':data})  

def payheads(request):
    data=Create_attendence.objects.all()
    return render(request,'payheads.html',{'p':data})   


def add_payhead(request):
    if request.method=='POST':
        name=request.POST['name']
        alias=request.POST['alias']
        pay_head_type=request.POST['payhead']
        income_type=request.POST['income']
        under=request.POST['under']
        affect_net_salary=request.POST['netsalary']
        payslip=request.POST['payslip']
        calculation_of_gratuity=request.POST['caltype']
        calculation_period=request.POST['ctype']
        calculation_type=request.POST['caltype']
        attendence_leave_withpay=request.POST['attendence with pay']
        attendence_leave_with_outpay=request.POST['Attendance with out pay']
        emp_add2duction_type=request.POST['ptype']
        opening_balance=request.POST['balance']
       

        #compute information
        compute=request.POST['compute']
        effective_from=request.POST['effective_from']
        # amount_greaterthan=request.POST['', False]
        amount_upto=request.POST['amount_upto']
        slabtype=request.POST['slab_type']
        value=request.POST['value']

        #Rounding
        round_method=request.POST['roundmethod']
        limit=request.POST['limit']

        #Gratuity
        days_of_months=request.POST['days_of_months']
        from_date=request.POST['from']
        to=request.POST['to']
        calculation_per_year=request.POST['eligiibility']

        std=create_payhead(name=name,
                           alias=alias,
                           pay_type=pay_head_type,
                           income_type=income_type,
                           under=under,
                           affect_net=affect_net_salary,
                           payslip=payslip,
                           calculation_of_gratuity=calculation_of_gratuity,
                           cal_type=calculation_type,
                           calculation_period=calculation_period,
                           leave_withpay=attendence_leave_withpay,
                           leave_with_out_pay=attendence_leave_with_outpay,
                           production_type=emp_add2duction_type,
                           opening_balance=opening_balance,
                           
        )
        std.save()
        idd=std

        std2=compute_information(Pay_head_id=idd,
                                 compute=compute,
                                 effective_from=effective_from,
                                #  amount_greater=amount_greaterthan,
                                 amount_upto=amount_upto,
                                 slab_type=slabtype,
                                 value=value,
        )
        std2.save()

        std3=Rounding(pay_head_id=idd,
                     Rounding_Method=round_method,
                     Round_limit=limit,
        )
        std3.save()

        std4=gratuity(pay_head_id=idd,
                     days_of_months=days_of_months,
                     number_of_months_from=from_date,
                     to=to,
                     calculation_per_year=calculation_per_year,
        )
        std4.save()
        messages.success(request,'successfully Added !!!')
        return redirect('alter_payrol_payheads')


def alter_payrol_payhead_edit2(request,pk):
    if request.method=='POST':
        data=create_payhead.objects.get(id=pk)
        data.name=request.POST.get('name')
        data.alias=request.POST.get('alias')
        data.pay_type=request.POST.get('payhead')
        data.income_type=request.POST.get('income')
        data.under=request.POST.get('under')
        data.affect_net=request.POST.get('netsalary')
        data.payslip=request.POST.get('payslip')
        data.calculation_of_gratuity=request.POST.get('caltype')
        data.cal_type=request.POST.get('ctype')
        data.calculation_period=request.POST.get('caltype')
        data.leave_withpay=request.POST.get('attendence with pay')
        data.leave_with_out_pay=request.POST.get('Attendance with out pay')
        data.production_type=request.POST.get('ptype')
        data.opening_balance=request.POST.get('balance')
        data.save()

        idd=data

        data2=compute_information.objects.get(id=pk)
        data2.compute=request.POST.get('compute')
        data2.effective_from=request.POST.get('effective_from')
        data2.amount_upto=request.POST.get('amount_upto')
        data2.slab_type=request.POST.get('slab_type')
        data2.value=request.POST.get('value')
        data2.Pay_head_id=idd

        data2.save()


        data3=Rounding.objects.get(id=pk)
        data3.Rounding_Method=request.POST.get('roundmethod')
        data3.Round_limit=request.POST.get('limit')
        data3.pay_head_id=idd
        data3.save()

        data4=gratuity.objects.get(id=pk)
        data4.days_of_months=request.POST.get('days_of_months')
        data4.number_of_months_from=request.POST.get('from')
        data4.to=request.POST.get('to')
        data4.calculation_per_year=request.POST.get('eligiibility')
        data4.pay_head_id=idd
        data4.save()
        return redirect('alter_payrol_payheads')
    return render(request,'alter_payrol_payhead_edit.html')
    

def alter_payrol_payhead_edit(request,pk):
    data=create_payhead.objects.get(id=pk)
    data2=compute_information.objects.get(id=pk)
    data3=Rounding.objects.get(id=pk)
    data4=gratuity.objects.get(id=pk)
    context={'p':data,'p2':data2,
    'p3':data3,'p4':data4
    }
    return render(request,'alter_payrol_payhead_edit.html',context) 



        
    
    #attendence 



def attendence(request):
    std=Create_attendence.objects.all()
    pk=units.objects.all()
    return render(request,'attendence.html',{'std':std,'pk':pk}) 

def emp_attendence(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method == 'POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        type=request.POST['type']
        period=request.POST['period']
        units1=request.POST['units']
        
        std=Create_attendence(
            name =name,
            alias=alias,
            under=under,
            type=type,
            period=period,
            units=units1,
           )
        std.save()
        messages.success(request,'successfully Added !!!')
        return redirect('alter_payrol_attendence')
    return render(request,'attendence.html',{'tally':tally})  

def attendence2(request):
    std=Create_attendence.objects.all()
    pk=units.objects.all()
    return render(request,'attendence_secondary.html',{'std':std,'pk':pk})
  




def alter_payrol_attendence3(request):
    if request.method == 'POST':
        name=request.POST['name']
        alias=request.POST['alias']
        under=request.POST['under']
        type=request.POST['type']
        
        std=Create_attendence(
            name =name,
            alias=alias,
            under=under,
            type=type,
           )
        std.save()
        messages.success(request,'successfully Added !!!')
        return redirect('alter_payrol_attendence')


def alter_payrol_attendence_edit(request,pk):
    data=Create_attendence.objects.get(id=pk)
    data2=Create_attendence.objects.all()
    pk=units.objects.all()
    context={'p':data,
    'std':data2,'pk':pk}
    return render(request,'alter_payrol_attendence_edit.html',context) 

def alter_payrol_attendence_edit2(request,pk):
    if request.method == 'POST':
        data=Create_attendence.objects.get(id=pk)
        data.name=request.POST.get('name')
        data.alias=request.POST.get('alias')
        data.under=request.POST.get('under')
        data.type=request.POST.get('type')
        data.period=request.POST.get('period')
        data.units=request.POST.get('units1')
        data.save()
        return redirect('alter_payrol_attendence')



    #employee


def employee(request):
    std=Create_employeegroup.objects.all()
    return render(request,'employe.html',{'std':std})

def addemployee(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        
        namee = request.POST['name']
        aliass = request.POST['alias']
        underr = request.POST['under']
        join = request.POST['join']
        sal = request.POST['sal']
        empname = request.POST['empname']
        desig = request.POST['desig']
        fn = request.POST['fn']
        loc = request.POST['loc']
        gen = request.POST['gen']
        dob = request.POST['dob']
        bloodd = request.POST['blood']
        prnts = request.POST['prnts']
        spouse = request.POST['spouse']
        adrs = request.POST['adrs']
        phone = request.POST['phone']
        email = request.POST['email']
        taxno = request.POST['taxno']
        aadhar = request.POST['aadhar']
        uan = request.POST['uan']
        pfn = request.POST['pfn']
        pran = request.POST['pran']
        esin = request.POST['esin']
        bank = request.POST['bank']
        #Bank
        
        acount=request.POST['acount']
        ifsc_code=request.POST['ifsc']
        bankname=request.POST['bank_name']
        branch=request.POST['branch_name']
        transaction_type=request.POST['Transaction_type']
        #E-found transfer
        acount_num=request.POST['acnumber']
        ifsc=request.POST['ifsccode']
        bankname2=request.POST['bank_name2']
        cheque=request.POST['cheque']


        
        
        std = Employee(

            name =namee,
            alias=aliass,
            under=underr,
            date_join=join,
            defn_sal =sal,
            emp_name = empname,
            emp_desg=desig ,
            fnctn = fn,
            location =loc,
            gender =gen,
            dob =dob,
            blood=bloodd,
            parent_name =prnts,
            spouse_name = spouse,
            address = adrs,
            number = phone,
            email = email,
            inc_tax_no = taxno,
            aadhar_no = aadhar,
            uan = uan,
            pfn = pfn,
            pran = pran,
            esin = esin,
            bankdtls = bank,
            
            



        )

        std.save()
        idd=std

        std2=add_bank(employee_id=idd,
                      Acount_No=acount,
                      IFSC_code=ifsc_code,
                      Bank_name=bankname,
                      Branch_name=branch,
                      Transaction_type=transaction_type,
        )
        std2.save()

        std3=E_found_trasfer(employee_id=idd,
                             Acount_No=acount_num,
                             IFSC_code=ifsc,
                             Bank_name=bankname2,
                             Cheque=cheque 
        )
        std3.save()
        return redirect('alter_payrol_employee')

def addemp_group2(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    std=Create_employeegroup.objects.all()
    if request.method == 'POST':
        name= request.POST['name']
        alias = request.POST['alias']
        under = request.POST['under']
        sal= request.POST['sal']

        std= Create_employeegroup(
            name =name,
            alias=alias,
            under=under,
            define_salary=sal,   
        )
        std.save()
        #messages.success(request,'employee group add successfully !!!')
        return redirect('employee')
    return render(request,'emp_group3.html',{'std':std,'tally':tally}) 

def alter_payrol_employee_edit(request,pk):
    std=Create_employeegroup.objects.all()
    p=Employee.objects.get(id=pk)
    p1=add_bank.objects.get(id=pk)
    p2=E_found_trasfer.objects.get(id=pk)
    return render(request,'alter_payrol_employee_edit.html',{'std':std,'p':p,'p1':p1,'p2':p2})

def alter_payrol_employee_edit2(request,pk):
    std=Employee.objects.get(id=pk)
    std.name=request.POST.get('name')
    std.alias=request.POST.get('alias')
    std.under=request.POST.get('under')
    std.date_join=request.POST.get('join')
    std.defn_sal=request.POST.get('sal')
    std.emp_name=request.POST.get('empname')
    std.emp_desg=request.POST.get('desig')
    std.fnctn=request.POST.get('fn')
    std.location=request.POST.get('loc')
    std.gender=request.POST.get('gen')
    std.dob=request.POST.get('dob')
    std.blood=request.POST.get('blood')
    std.parent_name=request.POST.get('prnts')
    std.spouse_name=request.POST.get('spouse')
    std.address=request.POST.get('adrs')
    std.number=request.POST.get('phone')
    std.email=request.POST.get('email')
    std.inc_tax_no=request.POST.get('taxno')
    std.aadhar_no=request.POST.get('aadhar')
    
    std.uan=request.POST.get('uan')
    std.pfn=request.POST.get('pfn')
    std.pran=request.POST.get('pran')
    std.esin=request.POST.get('esin')
    std.bankdtls=request.POST.get('bank')
    std.save()

    std1=add_bank.objects.get(id=pk)
    std1.Acount_No=request.POST.get('acount')
    std1.IFSC_code=request.POST.get('ifsc')
    std1.Bank_name=request.POST.get('bank_name')
    std1.Branch_name=request.POST.get('branch_name')
    std1.Transaction_type=request.POST.get('Transaction_type')
    std1.save()

    std2=add_bank.objects.get(id=pk)
    std2.Acount_No=request.POST.get('acnumber')
    std2.IFSC_code=request.POST.get('ifsccode')
    std2.Bank_name=request.POST.get('bank_name2')
    std2.Cheque=request.POST.get('cheque')
    std2.save()
    
    return redirect('alter_payrol_employee')


    


def salary1(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    pk=create_payhead.objects.all()
    if request.method=='POST':
        name1=request.POST['name']
        under=request.POST['under']
        effect=request.POST['effective']
        pay=request.POST['payhead']
        rate=request.POST['rate']
        per=request.POST['per']
        payhead=request.POST['payheaad_type']
        calculation=request.POST['calculation_type']
        #save salary
        std=salary(name=name1,
                   under=under,
                   effective=effect,
                   payhead=pay,
                   rate=rate,
                   per=per,
                   pay_type=payhead,
                   cal_type=calculation,
        )
        std.save()
        return redirect('salary1')
    return render(request,'salary.html',{'pk':pk}) 

def load(request):
    did=request.GET.get("id")
    obj=create_payhead.objects.get(name=did)
    return render(request,"load.html",{"obj":obj})

def load_calculation(request):
    did=request.GET.get("id")
    obj=create_payhead.objects.get(name=did)
    return render(request,"load_calculation.html",{"obj":obj})

  
  


def alter_payrol_employee(request):
    p3=Employee.objects.all()
    context={'data':p3}
    return render(request,'alter_payrol_employe2.html',context)   

def alter_payrol_employee2(request):
    obj=bank3.objects.all()
    data=Employee.objects.all()
    data2=empgroup2.objects.all()
    context={'std':data,
    'p':obj,'p3':data2}
    return render(request,'alter_payrol_employe.html',context)

def alter_payrol_addemployee(request):
    if request.method=='POST':
        
        namee = request.POST['name']
        aliass = request.POST['alias']
        underr = request.POST['underr']
        join = request.POST['join']
        sal = request.POST['sal']
        empname = request.POST['empname']
        desig = request.POST['desig']
        fn = request.POST['fn']
        loc = request.POST['loc']
        gen = request.POST['gen']
        dob = request.POST['dob']
        bloodd = request.POST['blood']
        prnts = request.POST['prnts']
        spouse = request.POST['spouse']
        adrs = request.POST['adrs']
        phone = request.POST['phone']
        email = request.POST['email']
        taxno = request.POST['taxno']
        aadhar = request.POST['aadhar']
        uan = request.POST['uan']
        pfn = request.POST['pfn']
        pran = request.POST['pran']
        esin = request.POST['esin']
        bank = request.POST['bank']
        #Bank
        acount=request.POST['acount']
        ifsc_code=request.POST['ifsc']
        bankname=request.POST['bank_name']
        branch=request.POST['branch_name']
        transaction_type=request.POST['Transaction_type']
        #E-found transfer
        acount_num=request.POST['acnumber']
        ifsc=request.POST['ifsccode']
        bankname2=request.POST['bank_name2']
        cheque=request.POST['cheque']


        
        
        std = Employee(

            name =namee,
            alias=aliass,
            under=underr,
            date_join=join,
            defn_sal =sal,
            emp_name = empname,
            emp_desg=desig ,
            fnctn = fn,
            location =loc,
            gender =gen,
            dob =dob,
            blood=bloodd,
            parent_name =prnts,
            spouse_name = spouse,
            address = adrs,
            number = phone,
            email = email,
            inc_tax_no = taxno,
            aadhar_no = aadhar,
            uan = uan,
            pfn = pfn,
            pran = pran,
            esin = esin,
            bankdtls = bank,
            
            



        )

        std.save()
        idd=std

        std2=add_bank(employee_id=idd,
                      Acount_No=acount,
                      IFSC_code=ifsc_code,
                      Bank_name=bankname,
                      Branch_name=branch,
                      Transaction_type=transaction_type,
        )
        std2.save()

        std3=E_found_trasfer(employee_id=idd,
                             Acount_No=acount_num,
                             IFSC_code=ifsc,
                             Bank_name=bankname2,
                             Cheque=cheque 
        )
        std3.save()
        return redirect('alter_payrol_employee')




#payrolvoucher

def payvoucher(request):
    return render(request,'payroll.html')   


def add_voucher(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method == 'POST':
        Vname = request.POST['name']
        alias = request.POST['alias']
        vtype = request.POST['type']
        abbre = request.POST['abber']
        activ_vou_typ = request.POST['active']  
        meth_vou_num = request.POST['numbering']
        useadv = request.POST.get('config', False)
        prvtdp = request.POST.get('prevent', False)
       
        allow_zero_trans = request.POST['trans']  
        provide_narr = request.POST['ledg']  
        print = request.POST['print']  
        
        std = create_VoucherModels(voucher_name=Vname ,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            provide_naration=provide_narr,
            print_voucher=print,

        )
        std.save()
        return redirect('alter_payrol_add_voucher2')

    return render(request, 'payroll.html',{'tally':tally})  



def alter_payrol_add_voucher(request):
    if request.method == 'POST':
        Vname = request.POST['name']
        alias = request.POST['alias']
        vtype = request.POST['type']
        abbre = request.POST['abber']
        activ_vou_typ = request.POST['active']  
        meth_vou_num = request.POST['numbering']
        useadv = request.POST.get('config', False)
        prvtdp = request.POST.get('prevent', False)
       
        
        allow_zero_trans = request.POST['trans']  
         
        print = request.POST['print']  
        
        std = create_VoucherModels(voucher_name=Vname ,
            alias=alias,
            voucher_type=vtype,
            abbreviation=abbre,
            active_this_voucher_type=activ_vou_typ,
            method_voucher_numbering=meth_vou_num,
            
            use_adv_conf = useadv,
            prvnt_duplictes =prvtdp,
            allow_zero_value_trns=allow_zero_trans,
            
            print_voucher=print,

        )
        std.save()
        return redirect('alter_payrol_add_voucher2')

    return render(request, 'alter_payrol_payroll.html')  


def alter_payrol_add_voucher2(request):
    emp=create_VoucherModels.objects.all()
    return render(request,'alter_payrol_payroll2.html',{'data':emp}) 

def alter_payrol_add_voucher3(request):
    emp=create_VoucherModels.objects.all()
    return render(request,'alter_payrol_payroll.html',{'data':emp}) 

def alter_payrol_add_voucher_edit(request,pk):
    emp=create_VoucherModels.objects.get(id=pk)
    data2=create_VoucherModels.objects.all()
    context={'p':emp,
    'data':data2}
    return render(request,'alter_payrol_payrolledit.html',context) 

def alter_payrol_add_voucher_edit2(request,pk):
    emp=create_VoucherModels.objects.get(id=pk)
    emp.voucher_name=request.POST.get('name')
    emp.alias=request.POST.get('alias')
    emp.voucher_type=request.POST.get('type')
    emp.abbreviation=request.POST.get('abber')
    emp.active_this_voucher_type=request.POST.get('active')
    emp.method_voucher_numbering=request.POST.get('numbering')
    emp.use_adv_conf=request.POST.get('config', False)
    emp.prvnt_duplictes=request.POST.get('prevent', False)
    emp.use_effective_date=request.POST.get('effect')
    emp.allow_zero_value_trns=request.POST.get('trans')
    emp.allow_naration_in_voucher=request.POST.get('narr')
    emp.make_optional=request.POST.get('optical')
    emp.provide_naration=request.POST.get('ledg')
    emp.print_voucher=request.POST.get('print')
    emp.save()
    return redirect('alter_payrol_add_voucher2')


    #unit




def alter_payrol_unit(request):
    p=units.objects.all()
    return render(request, 'alter_payrol_unit.html',{'p2':p})

def alter_payrol_unit2(request):
    p=units.objects.all()
    return render(request,'alter_payrol_unit2.html',{'data':p})

def stunits(request):   
    uq=unitQuantityCode.objects.all()
    ps=units.objects.all()
    return render(request,'stunits.html',{'ps':ps,'uq':uq})

def add_units(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        std=units()
        std.type=request.POST.get('type')
        std.symbol=request.POST.get('symbol')  
        std.formal_name=request.POST.get('formal')
        std.uqc1=request.POST.get('uqc1')
        std.number_of_decimal_places=request.POST.get('decimal') 
        std.first_unit=request.POST.get('ft1')
        std.conversion=request.POST.get('con')
        std.second_unit=request.POST.get('sec')  
        std.save()
        print('hai')
        return redirect('alter_payrol_unit2')
    return render(request,'stunits2.html',{'tally':tally}) 

def uqcform(request):
    if 't_id' in request.session:
        if request.session.has_key('t_id'):
            t_id = request.session['t_id']
        else:
            return redirect('/')
        tally = Companies.objects.filter(id=t_id)
    if request.method=='POST':
        uqname= request.POST['uqcname']
        u=unitQuantityCode(new_uqc=uqname)
        u.save()
    return render(request,'uqcform.html',{'tally':tally})   

def stunits2(request):
    ps=units.objects.all()
    uq=unitQuantityCode.objects.all()
    return render(request,'stunits2.html',{'ps':ps,'uq':uq}) 


def unit3(request):
    p=units.objects.all()
    return render(request,'unit3.html',{'data':p})




def alter_payrol_unit_edit(request,pk):
    uq=unitQuantityCode.objects.all()
    ps=units.objects.all()
    std=units.objects.get(id=pk)
    return render(request,'alter_payrol_unit_edit.html',{'ps':ps,'uq':uq,'std':std})

def alter_payrol_unit_edit2(request,pk):
    std=units.objects.get(id=pk)
    std.type=request.POST.get('type')
    std.symbol=request.POST.get('symbol')  
    std.formal_name=request.POST.get('formal')
    std.uqc1=request.POST.get('uqc1')
    std.number_of_decimal_places=request.POST.get('decimal') 
    std.first_unit=request.POST.get('ft1')
    std.conversion=request.POST.get('con')
    std.second_unit=request.POST.get('sec')  
    std.save()
    print('hai')
    return redirect('alter_payrol_unit2')


    






    #pan


def alter_statutory_panadd(request):
    if request.method == 'POST':
        tax2=request.POST['tax']
        no2=request.POST['no']

        std = pan(tax3 = tax2,
        no = no2)
        std.save()
        return redirect('alter_statutory_pan2')
    return render(request, 'alter_statutory_pan.html')




    #gst


def alter_statutory_gst3(request):
    return render(request,'alter_statutory_gst.html') 


def alter_statutory_gst2(request):
    if request.method == 'POST':
        state=request.POST['state']
        type=request.POST['type']
        teretory = request.POST['teretory']
        uin = request.POST['uin']
        gstr1 = request.POST['gstr1']
        kerala = request.POST['kerala']
        set = request.POST['set']
        enable = request.POST['enable']
        enable2 = request.POST['enable2']
        enable3 = request.POST['enable3']
        bond = request.POST['bond']
        taxrate = request.POST['taxrate']
        basistax = request.POST['basistax']
        purchase = request.POST['purchase']
        eway = request.POST['eway']
        applicable = request.POST['applicable']
        thresholt = request.POST['thresholt']
        limit = request.POST['limit']
        infrastate = request.POST['infrastate']
        thresholt2 = request.POST['thresholt2']
        invoice = request.POST['invoice']
        einvoice = request.POST['einvoice']

        std=gst(state=state,type=type,teretory=teretory,uin=uin,gstr1=gstr1,kerala=kerala,set=set,enable=enable,
        enable2=enable2,enable3=enable3,bond=bond,taxrate=taxrate,basistax=basistax,purchase=purchase,
        eway=eway,applicable=applicable,thresholt=thresholt,limit=limit,infrastate=infrastate,thresholt2=thresholt2,
        invoice=invoice,einvoice=einvoice)

        std.save()
        return redirect('alter_statutory_gst3')
        



#salary



def alter_payrol_salary(request):
    p=create_payhead.objects.all()
    return render(request,'alter_payrol_salary.html',{'pay':p}) 

def alter_payrol_salary2(request):
    data2=empgroup2.objects.all()
    return render(request,'alter_payrol_salary2.html',{'data':data2}) 

def alter_payrol_salary3(request):
    pk=create_payhead.objects.all()
    if request.method=='POST':
        name2=request.POST['name']
        under=request.POST['under']
        effect=request.POST['effective']
        pay=request.POST['payhead']
        rate=request.POST['rate']
        per=request.POST['per']
        payhead=request.POST['payheaad_type']
        calculation=request.POST['calculation_type']
        #save salary
        std=create_salary(name=name2,
                   under=under,
                   effective=effect,
                   payhead=pay,
                   rate=rate,
                   per=per,
                   payheaad_type=payhead,
                   calculation_type=calculation,
        )
        std.save()
        return redirect('alter_payrol_salary')
    return render(request,'alter_payrol_salary.html',{'pk':pk})






def alter_payrol_load(request):
    did=request.GET.get("id")
    print("id")
    obj=create_payhead.objects.get(name=did)
    return render(request,"alter_payrol_load.html",{"obj":obj})

def alter_payrol_load_calculation(request):
    did=request.GET.get("id")
    obj=create_payhead.objects.get(name=did)
    return render(request,"alter_payrol_load_calculation.html",{"obj":obj})





def bank(request):
    obj=bank3.objects.all()
    return render(request,"bank.html",{"p":obj})

def add_bank3(request):
    obj=bank3.objects.all()
    if request.method=="POST":
        nam=request.POST['name']
        std=bank3(name=nam)
        std.save()
        return redirect('employee2')



                







