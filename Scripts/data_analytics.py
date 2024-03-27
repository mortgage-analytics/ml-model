import numpy as np
from Timeline import Timeline
from datetime import datetime

# from Scripts.Timeline import calculate_differences

def getStage(applications, stageName):
    stageArray = []
    noneCount = 0
    for application in applications:
        if application[stageName] is not None:
            stageArray.append(application[stageName])
        else:
            noneCount += 1
    population = 1 - (noneCount/ (len(stageArray) + noneCount))
    return stageArray, round(population * 100, 2)

def stageAverageAndSD(applications, stage):
    stageArray, population = getStage(applications, stage)
    return np.mean(stageArray), np.std(stageArray), population

def rankForEachStage(applications, stage):
    stageArray, population = getStage(applications, stage)
    return sorted(stageArray), population

def WhatType(clients):
    AIP_Expected_Count = 0
    AIP_Granted_Count = 0
    Closed_Count = 0
    InfoGathering_Count = 0
    LoanOfferRec_Count = 0
    Not_Proceeding_Count = 0
    OnHold_Count = 0
    PreCompletion_Count = 0
    PreLoanOffer_Count = 0
    for client in clients:
        if client.application_status == "AIP expected":
            AIP_Expected_Count += 1
        elif client.application_status == "AIP granted":
            AIP_Granted_Count += 1
        elif client.application_status == "Closed":
            Closed_Count += 1
        elif client.application_status == "Information gathering":
            InfoGathering_Count += 1
        elif client.application_status == "Loan Offer received":
            LoanOfferRec_Count += 1
        elif client.application_status == "Not proceeding":
            Not_Proceeding_Count += 1
        elif client.application_status == "On hold":
            OnHold_Count += 1
        elif client.application_status == "Pre-completion":
            PreCompletion_Count += 1
        elif client.application_status == "Pre-Loan Offer":
            PreLoanOffer_Count += 1
    return AIP_Expected_Count,AIP_Granted_Count,Closed_Count,InfoGathering_Count,LoanOfferRec_Count,Not_Proceeding_Count,OnHold_Count,PreCompletion_Count,PreLoanOffer_Count

def SingleOrJoint(clients):
    singleCount = 0
    jointCount = 0
    for client in clients:
        if client.application_type == "Single":
            singleCount += 1
        elif client.application_type == "Joint":
            jointCount += 1
    return singleCount,jointCount

def WhatBank(clients):
    ICSCount = 0
    HavenCount = 0
    BOICount = 0
    AvantCount = 0
    FinanceIrelandCount = 0
    KBCCount = 0
    OtherCount = 0
    PermanentTSBCOunt = 0
    UlsterCount = 0
    for client in clients:
        if client.aip_lender_submitted_to == "ICS Mortgages":
            ICSCount += 1
        elif client.aip_lender_submitted_to == "Haven":
            HavenCount += 1
        elif client.aip_lender_submitted_to == "Bank of Ireland":
            BOICount += 1
        elif client.aip_lender_submitted_to == "Avant Money":
            AvantCount += 1
        elif client.aip_lender_submitted_to == "Finance Ireland":
            FinanceIrelandCount += 1
        elif client.aip_lender_submitted_to == "KBC":
            KBCCount += 1
        elif client.aip_lender_submitted_to == "Ulster Bank":
            UlsterCount += 1
        elif client.aip_lender_submitted_to == "Permanent TSB":
            UlsterCount += 1
        else:
            OtherCount += 1
    return ICSCount,HavenCount,BOICount,AvantCount,FinanceIrelandCount,KBCCount,OtherCount,PermanentTSBCOunt,UlsterCount

def IncomeOfCompletedMortgages(clients):
    averages = []
    lowest = float('inf')  # Use infinity as the initial lowest value
    highest = 0  # Initialize highest as 0, assuming all incomes are positive

    for client in clients:
        if client.application_status == "Closed" and client.application_stage == "COMPLETE":
            income = client.sum_of_income
            if income is not None and not np.isnan(income) and income > 0:
                averages.append(income)
                if income < lowest:
                    lowest = income
                if income > highest:
                    highest = income
    if averages:
        mean = np.nanmean(averages)
        std_dev = np.nanstd(averages, ddof=1)  
        lowest = None if lowest == float('inf') else lowest
    else:
        mean, std_dev = float('nan'), float('nan')
        lowest, highest = 'No data', 'No data'
    return mean, std_dev, highest, lowest

def _num_of_days2(date1, date2):
    date_format = "%d/%m/%Y"  # Ensure the format matches your date strings
    try:
        a = datetime.strptime(date1, date_format)
        b = datetime.strptime(date2, date_format)
        return (b - a).days
    except ValueError:
        return None

def AverageTimeToCompletion(clients):
    daysToCompletion = []
    for client in clients:
        lead_created_date = client.application.lead_created_date
        offer_letter_received_date = client.application.offer_letter_received_date
        if lead_created_date and isinstance(offer_letter_received_date, str) and offer_letter_received_date.lower() != 'nan':
            duration = _num_of_days2(lead_created_date, offer_letter_received_date)
            if duration is not None:  # Ensure duration is a valid number
                daysToCompletion.append(duration)
    valid_durations = [day for day in daysToCompletion if day is not None]
    if valid_durations:
        mean = np.mean(valid_durations)  # Now you can directly use np.mean
        std_dev = np.std(valid_durations)
        return f"{mean:.2f}",f"{std_dev:.2f}"
    else:
        return 'No data'
# getStage:
#   Takes in an array of type Application and the stage of the application
#   we are looking for as a string. 
#   Returns an array of type integer with the durations of that stage for each application 
#   and a population expressed as a percentage that tells us how many applications are in that stage.

# def getStage(applications, stageName):
#     stageArray = []
#     noneCount = 0
#     for applicationTimeline in applications:
#         diffs = {}
#         # diffs = applicationTimeline.calculate_differences()
#         if diffs.get(stageName) is not None:
#            stageArray.append(diffs.get(stageName)) 
#         else:
#             noneCount += 1
#     population = 1 - (noneCount / (len(stageArray) + noneCount))
#     return stageArray, population

# def stageAverageAndSD(applications, stage):
#     stageArray, population = getStage(applications, stage)
#     return np.mean(stageArray), np.std(stageArray), population

# def rankForEachStage(applications, stage):
#     stageArray, population = getStage(applications, stage)
#     return sorted(stageArray), population

# def singleOrJointClient(clients):
#     for client in clients:
#         if 

# # def stoppingStage(applications):
# #     for application in applications:
# #         currentStage = getattr(application, c) # what is the exact name of this

# def stageForAgents(agents, stage):
    
#     return