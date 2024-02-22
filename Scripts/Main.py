import pandas as pd
from Timeline import Timeline
from Client import Client

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
    for i in range(0, len(response_date)):
        timeline = Timeline(lead_created_date[i], application_created_date[i],
                            advisor_review_completion_date[i], submission_date[i], response_date[i],
                            valuation_received[i],
                            loan_offer_received[i], completed_date[i])
        applicationArray.append(timeline)
        # print(timeline)

    diffsArray = []
    for application in applicationArray:
        diffs = application.calculate_differences()
        diffsArray.append(diffs)

    clientsArray = []
    for i in range(0, len(submitted_to)):
        client = Client(type_[i], submitted_to[i], property_identified[i], mortgage_amount_proposed[i],single_joint[i])
        clientsArray.append(client)
        client.display_info()

    stage_name = 'lead_to_app'
    average, standard_dev,population = applicationArray[0].stageAverageAndSD(diffsArray,stage_name)
    print(f"Average for {stage_name}: {average}")
    print(f"Standard deviation for {stage_name}: {standard_dev}")

    stage_name = 'app_to_advisor'
    average, standard_dev,population = applicationArray[0].stageAverageAndSD(diffsArray, stage_name)
    print(f"Average for {stage_name}: {average}")
    print(f"Standard deviation for {stage_name}: {standard_dev}")

    stage_name = 'advisor_to_submission'
    average, standard_dev, population = applicationArray[0].stageAverageAndSD(diffsArray, stage_name)
    print(f"Average for {stage_name}: {average}")
    print(f"Standard deviation for {stage_name}: {standard_dev}")

    stage_name = 'submission_to_response'
    average,standard_dev, population = applicationArray[0].stageAverageAndSD(diffsArray, stage_name)
    print(f"Average for {stage_name}: {average}")
    print(f"Standard deviation for {stage_name}: {standard_dev}")

    stage_name = 'response_to_valuation'
    average,standard_dev, population = applicationArray[0].stageAverageAndSD(diffsArray, stage_name)
    print(f"Average for {stage_name}: {average}")
    print(f"Standard deviation for {stage_name}: {standard_dev}")

    stage_name = 'valuation_to_loan_offer'
    average,standard_dev, population = applicationArray[0].stageAverageAndSD(diffsArray, stage_name)
    print(f"Average for {stage_name}: {average}")
    print(f"Standard deviation for {stage_name}: {standard_dev}")

    stage_name = 'loan_offer_to_completed'
    average,standard_dev, population = applicationArray[0].stageAverageAndSD(diffsArray, stage_name)
    print(f"Average for {stage_name}: {average}")
    print(f"Standard deviation for {stage_name}: {standard_dev}")

    stage_name = 'loan_offer_to_completed'
    average, population = applicationArray[0].rankForEachStage(diffsArray, stage_name)
    print(f"Ranking for {stage_name}: {average}")

    FTBCount, STBCount, SwitchingCount, EquityCount = clientsArray[0].WhatType(clientsArray)

    ICSCount,HavenCount,BOICount,OtherCount = clientsArray[0].WhatBank(clientsArray)

    singleCount,jointCount = clientsArray[0].SingleOrJoint(clientsArray)

    print(f"We have {singleCount} single clients and {jointCount} joint clients")
    print(f"We have {FTBCount} first time buyers, {STBCount} second time buyers, {SwitchingCount} switching customers and {EquityCount} equity customers")
    print(f"We have {ICSCount} customers from ics,{HavenCount} customers from haven, {BOICount} customers from BOI and {OtherCount} from other banks")




    # for key, value in diffs.items():
    #     # print(f"{key}: {value}")
    #
    #     stats = timeline.calculate_stats(diffs)
    #
    #     for stage, stat in stats.items():
    #         pass
    #         # print(f"{stage}: Average = {stat['average']}, Standard Deviation = {stat['standard_deviation']}")
