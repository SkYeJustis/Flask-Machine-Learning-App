from flask import Flask, render_template, request, redirect, url_for

import pickle
import pandas as pd
from engineer_bank_features import determine_marital, determine_job, determine_edu, \
    determine_default, determine_loan, determine_contact, determine_poutcome, determine_month, \
    convert_to_yn, \
    determine_gender, determine_married, determine_edu_cat, determine_self_emp, \
    determine_prop_area, determine_dependent

from prediction_helpers import auc

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def home():
    if request.method == 'POST':
        selectedValue = request.form['option']
        return redirect(url_for('click', selectedValue=selectedValue))
    return render_template('home.html')

@app.route('/<selectedValue>')
def click(selectedValue):
    return render_template(selectedValue)


@app.route('/getSubscriptionOutcome', methods=['POST','GET'] )
def get_subscription_outcome():
    if request.method=='POST':
        result=request.form

        age = result['age']
        job = result['job']
        marital = result['marital']
        education = result['education']
        default = result['default']
        balance = result['balance']
        housing = result['housing']
        loan = result['loan']
        contact = result['contact']
        day = result['day']
        month = result['month']
        duration = result['duration']
        campaign = result['campaign']
        pdays = result['pdays']
        previous = result['previous']
        poutcome = result['poutcome']

        input_vec = [age, job, marital, education, default,
                     balance, housing, loan, contact, day,
                     month, duration, campaign, pdays,
                     previous, poutcome]
        col_names = ['age', 'job', 'marital', 'education', 'default',
                     'balance', 'housing', 'loan', 'contact', 'day',
                     'month', 'duration', 'campaign', 'pdays',
                     'previous', 'poutcome']

        input_df = pd.DataFrame(input_vec, col_names)
        input_df = input_df.transpose()

        job_list = ['job_admin.', 'job_blue-collar',
                    'job_entrepreneur', 'job_housemaid',
                    'job_management', 'job_retired',
                    'job_self-employed', 'job_services',
                    'job_student', 'job_technician',
                    'job_unemployed']
        for job in job_list:
            input_df[job] = 0

        marital_list = ['marital_divorced', 'marital_married',
                        'marital_single']
        for marital in marital_list:
            input_df[marital] = 0

        edu_list = ['education_primary', 'education_secondary',
                    'education_tertiary']
        for edu in edu_list:
            input_df[edu] = 0

        def_list = ['default_yes']
        for default in def_list:
            input_df[default] = 0

        loan_list = ['loan_yes']
        for loan in loan_list:
            input_df[loan] = 0

        cont_list = ['contact_cellular', 'contact_telephone']
        for cont in cont_list:
            input_df[cont] = 0

        pout_list = ['poutcome_failure', 'poutcome_other',
                     'poutcome_success']
        for pout in pout_list:
            input_df[pout] = 0

        month_list = ['month_apr', 'month_aug',
                      'month_feb', 'month_jan',
                      'month_jul', 'month_jun',
                      'month_mar', 'month_may',
                      'month_nov', 'month_oct', 'month_sep']
        for month in month_list:
            input_df[month] = 0

        determine_marital(input_df)
        determine_job(input_df)
        determine_edu(input_df)
        determine_default(input_df)
        determine_loan(input_df)
        determine_contact(input_df)
        determine_poutcome(input_df)
        determine_month(input_df)

        input_df = input_df[['age', 'balance', 'day', 'duration', 'campaign', 'pdays',
                             'previous', 'job_admin.', 'job_blue-collar',
                             'job_entrepreneur', 'job_housemaid', 'job_management', 'job_retired',
                             'job_self-employed', 'job_services', 'job_student', 'job_technician',
                             'job_unemployed', 'marital_married', 'marital_single',
                             'education_primary', 'education_secondary', 'education_tertiary',
                             'default_yes', 'loan_yes', 'contact_cellular', 'contact_telephone',
                             'poutcome_failure', 'poutcome_other', 'poutcome_success', 'month_apr',
                             'month_aug', 'month_feb', 'month_jan', 'month_jul', 'month_jun',
                             'month_mar', 'month_may', 'month_nov', 'month_oct', 'month_sep']]

        model_type = False


        if model_type:
            # load the model - random forest
            pkl_file = open('bank-marketing-sklearn-rf.pkl', 'rb')
            rfmodel = pickle.load(pkl_file)
            prediction = rfmodel.predict(input_df.values)

            return render_template('term_deposit_result.html',
                                   prediction=prediction[0])
        else:

            # load the model - keras
            from keras.models import load_model

            nn = load_model('bank-marketing-keras-nn.h5',
                            custom_objects={'auc': auc})

            input_df = input_df.as_matrix()
            y_pred = nn.predict(input_df)
            y_pred[y_pred <= 0.5] = 0.
            y_pred[y_pred > 0.5] = 1.
            y_pred.tolist()[0][0]

            prediction = convert_to_yn(y_pred.tolist()[0][0])
            return render_template('term_deposit_result.html',
                                   prediction=prediction)


@app.route('/getLoanOutcome', methods=['POST','GET'] )
def get_loan_outcome():
    if request.method=='POST':
        result=request.form

        Gender = result['Gender']
        Married = result['Married']
        Dependents = result['Dependents']
        Education = result['Education']
        Self_Employed = result['Self_Employed']
        ApplicantIncome = result['ApplicantIncome']
        CoapplicantIncome = result['CoapplicantIncome']
        LoanAmount = result['LoanAmount']
        Loan_Amount_Term = result['Loan_Amount_Term']
        Credit_History = result['Credit_History']
        Property_Area = result['Property_Area']


        input_vec = [Gender, Married, Dependents, Education, Self_Employed,
                     ApplicantIncome, CoapplicantIncome, LoanAmount, Loan_Amount_Term,
                     Credit_History, Property_Area]

        col_names = ['Gender', 'Married', 'Dependents', 'Education', 'Self_Employed',
                     'ApplicantIncome', 'CoapplicantIncome', 'LoanAmount', 'Loan_Amount_Term',
                     'Credit_History', 'Property_Area']

        input_df = pd.DataFrame(input_vec, col_names)
        input_df = input_df.transpose()



        gender_list = ['Gender_Female']
        for gender in gender_list:
            input_df[gender] = 0

        marital_list = ['Married_Yes']
        for marital in marital_list:
            input_df[marital] = 0

        edu_list = ['Education_Graduate']
        for edu in edu_list:
            input_df[edu] = 0

        self_employed_list = ['Self_Employed_Yes']
        for self_employed in self_employed_list:
            input_df[self_employed] = 0

        property_area_list = ['Property_Area_Rural', 'Property_Area_Urban']
        for property_area in property_area_list:
            input_df[property_area] = 0

        dep_list = ['Dependents_0', 'Dependents_1', 'Dependents_2']
        for dep in dep_list:
            input_df[dep] = 0

        determine_gender(input_df)
        determine_married(input_df)
        determine_edu_cat(input_df)
        determine_self_emp(input_df)
        determine_prop_area(input_df)
        determine_dependent(input_df)


        input_df = input_df[['ApplicantIncome', 'CoapplicantIncome', 'LoanAmount',
                             'Loan_Amount_Term', 'Credit_History', 'Gender_Female', 'Married_Yes',
                             'Education_Graduate', 'Self_Employed_Yes', 'Property_Area_Rural',
                             'Property_Area_Urban', 'Dependents_0', 'Dependents_1', 'Dependents_2']]

        model_type = False


        if model_type:
            # load the model - random forest
            pkl_file = open('bank-loan-sklearn-rf.pkl', 'rb')
            rf = pickle.load(pkl_file)
            prediction = rf.predict(input_df.values)

            return render_template('loan_result.html',
                                   prediction=prediction[0])
        else:

            # load the model - keras
            from keras.models import load_model

            nn = load_model('bank-loan-keras-nn.h5',
                            custom_objects={'auc': auc})

            input_df = input_df.as_matrix()
            y_pred = nn.predict(input_df)
            y_pred[y_pred <= 0.5] = 0.
            y_pred[y_pred > 0.5] = 1.
            y_pred.tolist()[0][0]

            prediction = convert_to_yn(y_pred.tolist()[0][0])
            return render_template('loan_result.html',
                                   prediction=prediction)

if __name__ == '__main__':
	app.debug = True
	app.run()