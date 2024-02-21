import pandas as pd

file_path = r'C:\Users\rober\OneDrive\Documents\College\SWENG\Loading_Data\Copy of combined_report-1707267132094.xlsx - Application Data (Import).csv'
df = pd.read_csv(file_path)

last_updated_date = df['Last Updated Date'].tolist()
last_logged_in = df['Last Logged In'].tolist()
type_ = df['Type'].tolist()
stage = df['Stage'].tolist()
property_identified = df['Property Identified'].tolist()
mortgage_amount_proposed = df['Mortgage Amount Proposed'].tolist()
lead_created_date = df['Lead Created Date'].tolist()
application_created_date = df['Application Created Date'].tolist()
advisor_review_completion_date = df['Advisor Review Completion Date'].tolist()
submission_date = df['Submission Date'].tolist()
response_date = df['Response Date'].tolist()
valuation_received = df['Valuation Received'].tolist()
loan_offer_received = df['Loan Offer Received'].tolist()
completed_date = df['Completed Date'].tolist()
status = df['Status'].tolist()
submitted_to = df['Submitted To'].tolist()
lead_source = df['Lead Source'].tolist()
assigned_to = df['Assigned To'].tolist()
single_joint = df['Single/Joint'].tolist()
