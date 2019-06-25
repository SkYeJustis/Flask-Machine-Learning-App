
def determine_marital(input_df):
    if input_df['marital'][0]=="divorced":
        input_df['marital_divorced'] = 1
    elif input_df['marital'][0]=="married":
        input_df['marital_married'] = 1
    elif input_df['marital'][0]=="single":
        input_df['marital_single']= 1
    else:
        pass

def determine_job(input_df):
    if input_df['job'][0]=="admin.":
        input_df['job_admin.'] = 1
    elif input_df['job'][0]=="unemployed":
        input_df['job_unemployed'] = 1
    elif input_df['job'][0]=="management":
        input_df['job_management']= 1
    elif input_df['job'][0]=="housemaid":
        input_df['job_housemaid']=1
    elif input_df['job'][0]=="entrepreneur":
        input_df['job_entrepreneur']=1
    elif input_df['job'][0]=="student":
        input_df['job_student']=1
    elif input_df['job'][0]=="blue-collar":
        input_df['job_blue-collar']=1
    elif input_df['job'][0]=="self-employed":
        input_df['job_self-employed']=1
    elif input_df['job'][0]=="retired":
        input_df['job_retired']=1
    elif input_df['job'][0]=="technician":
        input_df['job_technician']=1
    elif input_df['job'][0]=="services":
        input_df[ 'job_services']=1
    else:
        pass

def determine_edu(input_df):
    if input_df['job'][0]=="primary":
        input_df['education_primary'] = 1
    elif input_df['job'][0]=="secondary":
        input_df['education_secondary'] = 1
    elif input_df['job'][0]=="tertiary":
        input_df['education_tertiary']= 1
    else:
        pass

def determine_default(input_df):
    if input_df['default'][0]=="yes":
        input_df['def_yes'] = 1
    else:
        pass

def determine_loan(input_df):
    if input_df['loan'][0]=="yes":
        input_df['loan_yes'] = 1
    else:
        pass

def determine_contact(input_df):
    if input_df['contact'][0]=="cellular":
        input_df['contact_cellular'] = 1
    elif input_df['contact'][0]=="telephone":
        input_df['contact_telephone'] = 1
    else:
        pass


def determine_month(input_df):
    if input_df['month'][0] == "aug":
        input_df['month_aug'] = 1
    elif input_df['month'][0] == "feb":
        input_df['month_feb'] = 1
    elif input_df['month'][0] == "jan":
        input_df['month_jan'] = 1

    elif input_df['month'][0] == "jul":
        input_df['month_jul'] = 1
    elif input_df['month'][0] == "jun":
        input_df['month_jun'] = 1
    elif input_df['month'][0] == "mar":
        input_df['month_mar'] = 1

    elif input_df['month'][0] == "may":
        input_df['month_may'] = 1
    elif input_df['month'][0] == "nov":
        input_df['month_nov'] = 1
    elif input_df['month'][0] == "oct":
        input_df['month_oct'] = 1

    elif input_df['month'][0] == "sep":
        input_df['month_sep'] = 1
    elif input_df['month'][0] == "apr":
        input_df['month_apr'] = 1
    else:
        pass

def determine_poutcome(input_df):
    if input_df['poutcome'][0]=="failure":
        input_df['poutcome_failure'] = 1
    elif input_df['poutcome'][0]=="other":
        input_df['poutcome_other'] = 1
    elif input_df['poutcome'][0]=="success":
        input_df['poutcome_success'] = 1
    else:
        pass

def determine_gender(input_df):
    if input_df['Gender'][0]=="Female":
        input_df['Gender_Female'] = 1

def determine_married(input_df):
    if input_df['Married'][0]=="Yes":
        input_df['Married_Yes'] = 1

def determine_edu_cat(input_df):
    if input_df['Education'][0]=='Graduate':
        input_df['Education_Graduate'] = 1

def determine_self_emp(input_df):
    if input_df['Self_Employed'][0]=="Yes":
        input_df['Self_Employed_Yes'] = 1

def determine_prop_area(input_df):
    if input_df['Property_Area'][0]=="Rural":
        input_df['Property_Area_Rural'] = 1
    elif input_df['Property_Area'][0]=="Urban":
        input_df['Property_Area_Urban'] = 1

def determine_dependent(input_df):
    if input_df['Dependents'][0]=="0":
        input_df['Dependents_0'] = 1
    elif input_df['Dependents'][0]=="1":
        input_df['Dependents_1'] = 1
    elif input_df['Dependents'][0]=="2":
        input_df['Dependents_2'] = 1

def convert_to_yn(input_char):
    if input_char == 0 or input_char == 'N':
        return 'No'
    else:
        return 'Yes'