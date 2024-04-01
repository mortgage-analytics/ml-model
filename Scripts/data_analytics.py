import numpy as np
from Scripts.Timeline import Timeline
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
    PermanentTSBCount = 0
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
            PermanentTSBCount += 1
        else:
            OtherCount += 1
    return ICSCount,HavenCount,BOICount,AvantCount,FinanceIrelandCount,KBCCount,OtherCount,PermanentTSBCount,UlsterCount

def IncomeOfCompletedMortgages(clients):
    averages = []
    lowest = float('inf')  
    highest = 0  

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
    date_format = "%d/%m/%Y"  
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
            if duration is not None:  
                daysToCompletion.append(duration)
    valid_durations = [day for day in daysToCompletion if day is not None]
    if valid_durations:
        mean = np.mean(valid_durations)  
        std_dev = np.std(valid_durations)
        return f"{mean:.2f}",f"{std_dev:.2f}"
    else:
        return 'No data'
    
def MortgageType(clients):
    NewHomeCount = 0 
    RemortgagingCount = 0
    for client in clients:
        if client.mortgage_type == "Purchasing a New Home":
            NewHomeCount += 1
        elif client.mortgage_type == "Remortgaging Existing Loan":
            RemortgagingCount += 1
    return NewHomeCount, RemortgagingCount

def PropertyValue(clients):
    values = []
    for client in clients:
        if client.property_value > 10000 and client.property_value < 30000000:
            values.append(client.property_value)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev    

def MortgageAmountProposed(clients):
    values = []
    for client in clients:
        if client.mortgage_amount_proposed > 10000 and client.mortgage_amount_proposed < client.property_value:
            values.append(client.mortgage_amount_proposed)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev    

def Applications(clients):
    AppCount = 0
    for client in clients:
        if client.lead_status=="Application":
            AppCount += 1
    return AppCount, len(clients)-AppCount

def InterestRateType(clients):
    FixedCount = 0
    VariableCount = 0
    for client in clients:
        if client.interest_rate_type == "Fixed":
            FixedCount+=1
        elif client.interest_rate_type == "Variable":
            VariableCount+=1
    return FixedCount, VariableCount


def CurrentLender(clients):
    AIBCount = 0
    HavenCount = 0
    BOICount = 0
    EBSCount = 0
    PepperCount = 0
    KBCCount = 0
    BlankCount = 0
    PTSBCount = 0
    UlsterCount = 0
    for client in clients:
        if client.aip_lender_submitted_to == "AIB":
            AIBCount += 1
        elif client.aip_lender_submitted_to == "Haven":
            HavenCount += 1
        elif client.aip_lender_submitted_to == "BOI":
            BOICount += 1
        elif client.aip_lender_submitted_to == "EBS":
            EBSCount += 1
        elif client.aip_lender_submitted_to == "Pepper":
            PepperCount += 1
        elif client.aip_lender_submitted_to == "KBC":
            KBCCount += 1
        elif client.aip_lender_submitted_to == "Ulster Bank":
            UlsterCount += 1
        elif client.aip_lender_submitted_to == "PTSB":
            PTSBCount += 1
        else:
            BlankCount += 1
    return AIBCount,HavenCount,BOICount,EBSCount,PepperCount,KBCCount,BlankCount,PTSBCount,UlsterCount

def CurrentInterestRate(clients):
    values = []
    for client in clients:
        if client.current_interest_rate>0:
            values.append(client.current_interest_rate)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev  

def CurrentMonthlyPayments(clients):
    values = []
    for client in clients:
        if client.current_monthly_payment>0:
            values.append(client.current_monthly_payment)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev  

def ChosenLenderProvider(clients):
    ICSCount = 0
    HavenCount = 0
    AvantCount = 0
    BlankCount = 0
    PermanentTSBCount = 0
    MortgageStoreCount = 0
    for client in clients:
        if client.aip_lender_submitted_to == "ICS Mortgages":
            ICSCount += 1
        elif client.aip_lender_submitted_to == "Haven":
            HavenCount += 1
        elif client.aip_lender_submitted_to == "Mortgage Store":
            MortgageStoreCount += 1
        elif client.aip_lender_submitted_to == "Avant Money":
            AvantCount += 1
        elif client.aip_lender_submitted_to == "Permanent TSB":
            PermanentTSBCount += 1
        else:
            BlankCount += 1
    return ICSCount,HavenCount,AvantCount,MortgageStoreCount,PermanentTSBCount,BlankCount

def GrossBasicIncome(clients):
    values = []
    for client in clients:
        if client.lead_gross_basic_income>=25000:
            values.append(client.lead_gross_basic_income)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev  

def documentationUploaded(clients):
    values = []
    for client in clients:
        if client.documents_uploaded:
            if client.primary_documents_percentage is not None:
                values.append(client.primary_documents_percentage)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev

def secondaryDocumentationUploaded(clients):
    values = []
    for client in clients:
        if client.secondary_documents_upload:
            if not np.isnan(client.secondary_documents_percentage):
                values.append(client.primary_documents_percentage)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev

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