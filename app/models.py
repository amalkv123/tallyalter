from django.db import models
from django.template.defaultfilters import slugify
from django.urls import reverse
from django.contrib.auth.models import User

class P_cost_default(models.Model):
    name=models.CharField(max_length=100,null=True,blank=True)
    alias=models.CharField(max_length=100,null=True,blank=True)
    revenue=models.CharField(max_length=50,null=True,blank=True)
    non_revenue=models.CharField(max_length=50,null=True,blank=True)

    def __str__(self):
        return self.name

class Create_employeegroup(models.Model):
    name =models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    define_salary=models.CharField(max_length=225) 

class emp_category(models.Model):
    cat_name= models.CharField(max_length=225)
    cat_alias= models.CharField(max_length=225)
    revenue_items=models.CharField(max_length=225)
    non_revenue_items=models.CharField(max_length=225)

class CreateEmployeeGrp(models.Model):
    name=models.CharField(max_length=100)
    alias=models.CharField(max_length=100)
    under_name=models.CharField(max_length=50)

class crtcompony(models.Model):
    componyname = models.CharField(max_length=50)
    mailingname = models.CharField (max_length=50)
    address = models.CharField (max_length=50)
    state = models.CharField (max_length=50)
    country = models.CharField (max_length=50)
    pincode = models.CharField (max_length=10)
    telphone = models.CharField(max_length=10)
    mobile = models.CharField(max_length=10)
    fax = models.CharField(max_length=10)
    email=models.EmailField()
    website=models.CharField(max_length=100)
    fyearbgn=models.DateField()
    booksbgn=models.DateField()
    curncysymbl=models.CharField(max_length=10)
    crncyname=models.CharField(max_length=10)

class empgroup(models.Model):
    name = models.CharField(max_length=50)
    alias = models.CharField (max_length=50)


class empgroup2(models.Model):
    groupname = models.CharField(max_length=50)
    groupalias = models.CharField (max_length=50)
    groupunder = models.CharField (max_length=50)



class Employee(models.Model):
    
    name = models.CharField(max_length=225)
    alias= models.CharField(max_length=225)
    under= models.CharField(max_length=225)
    date_join = models.DateField()
    defn_sal = models.CharField(max_length=225)
    emp_name = models.CharField(max_length=225)
    emp_desg = models.CharField(max_length=225)
    fnctn = models.CharField(max_length=225)
    location = models.CharField(max_length=225)
    gender= models.CharField(max_length=225)
    dob = models.DateField()
    blood = models.CharField(max_length=225)
    parent_name =models.CharField(max_length=225)
    spouse_name =models.CharField(max_length=225)
    address =models.CharField(max_length=225)
    number =models.CharField(max_length=225)
    email =models.CharField(max_length=225)
    inc_tax_no =models.CharField(max_length=225)
    aadhar_no=models.CharField(max_length=225)
    uan =models.CharField(max_length=225)
    pfn =models.CharField(max_length=225)
    pran =models.CharField(max_length=225)
    esin =models.CharField(max_length=225)
    bankdtls=models.CharField(max_length=225)

class salary(models.Model):
    name=models.CharField(max_length=225)
    under=models.CharField(max_length=225) 
    effective=models.CharField(max_length=225)
    payhead=models.CharField(max_length=225)
    rate=models.CharField(max_length=225)
    per=models.CharField(max_length=225)
    pay_type=models.CharField(max_length=225)
    cal_type=models.CharField(max_length=225)





class add_bank(models.Model):
    employee_id= models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    Acount_No=models.CharField(max_length=225)
    IFSC_code=models.CharField(max_length=225)
    Bank_name=models.CharField(max_length=225)
    Branch_name=models.CharField(max_length=225)
    Transaction_type=models.CharField(max_length=225)


class E_found_trasfer(models.Model):
    employee_id= models.ForeignKey(Employee, on_delete=models.CASCADE, null=True, blank=True)
    Acount_No=models.CharField(max_length=225)
    IFSC_code=models.CharField(max_length=225)
    Bank_name=models.CharField(max_length=225)
    Cheque=models.CharField(max_length=225)

class create_VoucherModels(models.Model):
    voucher_name = models.CharField(max_length=225)
    alias = models.CharField(max_length=225)
    voucher_type = models.CharField(max_length=225)
    abbreviation = models.CharField(max_length=225)
    active_this_voucher_type =  models.CharField(max_length=225)
    method_voucher_numbering = models.CharField(max_length=225)
    use_adv_conf = models.CharField(max_length=225,blank=True)
    prvnt_duplictes = models.CharField(max_length=225,default="Null",blank=True)
    use_effective_date =  models.CharField(max_length=225,default="Null")
    allow_zero_value_trns =  models.CharField(max_length=225)
    allow_naration_in_voucher =  models.CharField(max_length=225)
    make_optional =  models.CharField(max_length=225)
    provide_naration =  models.CharField(max_length=225)
    print_voucher = models.CharField(max_length=225)




class Create_attendence(models.Model):
    name =models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    type =models.CharField(max_length=225)
    period=models.CharField(max_length=225,default='null',blank=True)
    units=models.CharField(max_length=225,default='null',blank=True)   


class pan(models.Model):
    tax3 =models.IntegerField(max_length=225)
    no =models.IntegerField(max_length=225)


class create_payhead(models.Model):
    name=models.CharField(max_length=225)
    alias=models.CharField(max_length=225)
    pay_type=models.CharField(max_length=225)
    income_type=models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    affect_net=models.CharField(max_length=225)
    payslip=models.CharField(max_length=225)
    calculation_of_gratuity=models.CharField(max_length=225)
    cal_type=models.CharField(max_length=225)
    calculation_period=models.CharField(max_length=225)
    leave_withpay=models.CharField(max_length=225)
    leave_with_out_pay=models.CharField(max_length=225)
    production_type=models.CharField(max_length=225)
    opening_balance=models.CharField(max_length=225) 
    



class compute_information(models.Model):
    Pay_head_id = models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    compute=models.CharField(max_length=225,default="Null")
    effective_from=models.CharField(max_length=225,default="NULL")
    amount_greater=models.CharField(max_length=225,default="NULL")
    amount_upto=models.CharField(max_length=225,default="NULL")
    slab_type=models.CharField(max_length=225,default="NULL")
    value=models.CharField(max_length=225,default="NULL")



class Rounding(models.Model):
    pay_head_id = models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    Rounding_Method =models.CharField(max_length=225,default="Null",blank=True)
    Round_limit = models.CharField(max_length=22,default="Null",blank=True)


class gratuity(models.Model):
    pay_head_id=models.ForeignKey(create_payhead, on_delete=models.CASCADE, null=True, blank=True)
    days_of_months=models.CharField(max_length=225)
    number_of_months_from=models.CharField(max_length=225)
    to=models.CharField(max_length=225)
    calculation_per_year=models.CharField(max_length=225)   





class units(models.Model):
    type= models.CharField(max_length=225)
    symbol=models.CharField(max_length=225)
    formal_name=models.CharField(max_length=225)
    uqc1=models.CharField(max_length=225,default='null',blank=True)
    number_of_decimal_places=models.CharField(max_length=225)
    first_unit=models.CharField(max_length=225)
    conversion=models.CharField(max_length=225)
    second_unit=models.CharField(max_length=225)

class unitQuantityCode(models.Model):
    new_uqc=models.CharField(max_length=225)

class Companies(models.Model):
    d_path=models.CharField(max_length=100,null=True)
    name = models.CharField(max_length=255)
    mailing_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    state = models.CharField(max_length=255)
    country = models.CharField(max_length=255)
    pincode = models.CharField(max_length=10,null=True)
    telephone = models.CharField(max_length=20,null=True)
    mobile = models.CharField(max_length=15,null=True)
    fax = models.CharField(max_length=15,null=True)
    email = models.EmailField(null=True)
    password = models.CharField(max_length=240, null=True)
    website = models.CharField(max_length=100,null=True)
    currency_symbol = models.CharField(max_length=20)
    formal_name = models.CharField(max_length=20)
    fin_begin = models.DateField()
    books_begin = models.DateField()
    fin_end = models.DateField()
    status=models.BooleanField(default=True)



class gst(models.Model):
    state= models.CharField(max_length=225)
    type=models.CharField(max_length=225)
    teretory=models.CharField(max_length=225)
    uin=models.CharField(max_length=225)
    gstr1=models.CharField(max_length=225)
    kerala=models.CharField(max_length=225)
    set=models.CharField(max_length=225)
    enable= models.CharField(max_length=225)
    enable2=models.CharField(max_length=225)
    enable3=models.CharField(max_length=225)
    bond=models.CharField(max_length=225)
    taxrate=models.CharField(max_length=225)
    basistax=models.CharField(max_length=225)
    purchase=models.CharField(max_length=225)
    eway=models.CharField(max_length=225)
    applicable=models.CharField(max_length=225)
    thresholt=models.CharField(max_length=225)
    limit=models.CharField(max_length=225)
    infrastate=models.CharField(max_length=225)
    thresholt2=models.CharField(max_length=225)
    invoice=models.CharField(max_length=225)
    einvoice=models.CharField(max_length=225)



class create_salary(models.Model):
    name= models.CharField(max_length=225)
    under=models.CharField(max_length=225)
    effective = models.CharField(max_length=225)
    payhead=models.CharField(max_length=225)
    rate=models.CharField(max_length=225)
    per=models.CharField(max_length=225)
    payheaad_type=models.CharField(max_length=225)
    calculation_type=models.CharField(max_length=225)


class bank3(models.Model):
    name =models.CharField(max_length=225)
    



     


   
    