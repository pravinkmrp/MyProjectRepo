
from faker import Faker
fake = Faker()

import csv

add_loan = ("INSERT INTO pravin_loan_table "
            "(loan_number, borrower1_ssn, borrower2_ssn, seller_name, servicer_name, loan_amount, loan_balance_pending, "
            "borrower1_zip, borrower2_zip, seller_zip, servicer_zip, loan_creation_date, property_zip, property_type, "
            "property_value_initial, property_value_current, borrower1_state, borrower2_state, seller_state, servicer_state, "
            "loan_period_type, loan_margin_percentage, property_state, fraud) "
            "VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s, %s, %s, %s)")

field_names=["loan_number","borrower1_ssn","borrower2_ssn","seller_name","servicer_name","loan_amount","loan_balance_pending",
             "borrower1_zip","borrower2_zip","seller_zip","servicer_zip","loan_creation_date","property_zip","property_type",
                "property_value_initial","property_value_current","borrower1_state","borrower2_state","seller_state","servicer_state",
                "loan_period_type","loan_margin_percentage","property_state","fraud","borrower1_name","borrower2_name",
             "extra1","extra2","extra3","extra4","borrower1_dob","borrower2_dob"]

seller_servicer=['Bank of America', 'Wells Fargo', 'Chase', 'ABC bank', 'DEF bank', 'SBI Bank']

fbool=[1,0,None]
lptype=['15 YEAR', '30 YEAR']
ptype=['PRIMARY', 'INVESTMENT']

base=100000000

with open('loan_file_small_%s.csv' % str(base), mode='w') as loan_file:
    loan_writer = csv.writer(loan_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    loan_writer.writerow(field_names)
    for i in range(1,10000000):
        #loan_number=fake.random.randint(1999999999,9999999999)
        loan_number =base+i
        borrower1_ssn=fake.ssn().replace('-','')
        borrower1_name=fake.name()
        borrower2_name=fake.name()
        borrower2_ssn=fake.ssn().replace('-','')
        seller_name=fake.random.choice(seller_servicer)
        servicer_name=fake.random.choice(seller_servicer)
        loan_amount=fake.random.randint(0,99999999)
        loan_balance_pending=fake.random.randint(0,99999999)
        borrower1_zip=fake.postcode()
        borrower2_zip=fake.postcode()
        seller_zip=fake.postcode()
        servicer_zip=fake.postcode()
        loan_creation_date=fake.date()
        property_zip=fake.postcode()
        property_type=fake.random.choice(ptype)
        property_value_initial=fake.random.randint(0,99999999)
        property_value_current=fake.random.randint(0,99999999)
        borrower1_state=fake.state()
        borrower2_state=fake.state()
        seller_state=fake.state()
        servicer_state=fake.state()
        loan_period_type=fake.random.choice(lptype)
        loan_margin_percentage=fake.random.randint(0,60)
        property_state=fake.state()
        fraud=fake.random.choice(fbool)
        extra1=fake.job()
        extra2=fake.phone_number()
        extra3=fake.currency_name()
        extra4=fake.safe_email()
        borrower1_dob=fake.date_of_birth()
        borrower2_dob = fake.date_of_birth()


        loan_values = (loan_number, borrower1_ssn, borrower2_ssn, seller_name, servicer_name, loan_amount, loan_balance_pending,
                borrower1_zip, borrower2_zip, seller_zip, servicer_zip, loan_creation_date, property_zip, property_type,
                property_value_initial, property_value_current, borrower1_state, borrower2_state, seller_state, servicer_state,
                loan_period_type, loan_margin_percentage, property_state, fraud, borrower1_name, borrower2_name,
                       extra1,extra2,extra3,extra4,borrower1_dob,borrower2_dob)

        #print(add_loan % loan_values)
        loan_writer.writerow(loan_values)
