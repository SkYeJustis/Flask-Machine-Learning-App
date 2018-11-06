from flask import Flask, request, render_template
import pickle
import pandas as pd
from engineer_bank_features import determine_marital, determine_job, determine_edu, \
    determine_default, determine_loan, determine_contact, determine_poutcome, determine_month, \
    convert_to_yn
from prediction_helpers import auc

app = Flask(__name__)

@app.route('/')
def home():
	return render_template('home.html')

@app.route( '/getSubscriptionOutcome', methods=['POST','GET'] )
def get_delay():
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

            return render_template('result.html',
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
            return render_template('result.html',
                                   prediction=prediction)


if __name__ == '__main__':
	app.debug = True
	app.run()