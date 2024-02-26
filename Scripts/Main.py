import pandas as pd
from Timeline import Timeline
from Client import Client
import data_analytics

stagesNames = ['lead_to_app', 'app_to_advisor', 'advisor_to_submission', 'submission_to_response', 'response_to_valuation',
               'valuation_to_loan_offer', 'loan_offer_to_completed']


if __name__ == "__main__":
    file_path = r"../data.csv"
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

    applicationArray = []
    diffsArray = []
    clientsArray = []
    for i in range(0, len(response_date)):
        client = Client(type_[i], submitted_to[i], property_identified[i], mortgage_amount_proposed[i],single_joint[i], None)
        clientsArray.append(client)
        timeline = Timeline(lead_created_date[i], application_created_date[i],
                            advisor_review_completion_date[i], submission_date[i], response_date[i],
                            valuation_received[i], loan_offer_received[i], completed_date[i], client)
        applicationArray.append(timeline)
        diffsArray.append(timeline.calculate_differences())
        client.application = timeline
        client.display_info()

    for stageName in stagesNames:
        average, standardDev, population = data_analytics.stageAverageAndSD(diffsArray,stageName) 
        print(f"Average for {stageName}: {average}")
        print(f"Standard deviation for {stageName}: {standardDev}")
        print(f"This data was collected with {population}% of the available data") 

    FTBCount, STBCount, SwitchingCount, EquityCount = data_analytics.WhatType(clientsArray)

    ICSCount,HavenCount,BOICount,OtherCount = data_analytics.WhatBank(clientsArray)

    singleCount,jointCount = data_analytics.SingleOrJoint(clientsArray)

    print(f"We have {singleCount} single clients and {jointCount} joint clients")
    print(f"We have {FTBCount} first time buyers, {STBCount} second time buyers, {SwitchingCount} switching customers and {EquityCount} equity customers")
    print(f"We have {ICSCount} customers from ICS,{HavenCount} customers from Haven, {BOICount} customers from BOI and {OtherCount} from other banks")
