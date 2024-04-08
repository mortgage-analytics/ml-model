import numpy as np
from Scripts.Timeline import Timeline
from datetime import datetime

def getStage(applications, stageName):
    """
    Extracts values for a specified stage from a collection of applications and calculates the data completeness for that stage.
    Parameters:
    - applications (list of dicts): The collection of application records, where each record is a dictionary.
    - stageName (str): The key corresponding to the desired stage in the application records.
    Returns:
    -1. A list of non-None values for the specified stage across all applications.
    -2. The percentage of applications with non-None values for this stage, rounded to two decimal places.
    """
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
    """
    Counts the occurrences of each application status within a list of client records.

    Parameters:
    - clients (list): A list of client objects, where each object contains an 'application_status' attribute.

    Returns:
    - all the counts of the different status'
    """
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
    """
    Counts the number of single and joint applications within a list of client records.

    Parameters:
    - clients (list): A list of client objects, where each object has an 'application_type' attribute.

    Returns:
    - singleCount: The total number of single applications.
    - jointCount: The total number of joint applications.
    """
    singleCount = 0
    jointCount = 0
    for client in clients:
        if client.application_type == "Single":
            singleCount += 1
        elif client.application_type == "Joint":
            jointCount += 1
    return singleCount,jointCount

def WhatBank(clients):
    """
    Counts the number of applications submitted to various banks within a list of client records.

    Parameters:
    - clients (list): A list of client objects, where each object has an 'aip_lender_submitted_to' attribute.

    Returns:
    - ICSCount: Total number of applications submitted to ICS Mortgages.
    - HavenCount: Total number of applications submitted to Haven.
    - BOICount: Total number of applications submitted to Bank of Ireland.
    - AvantCount: Total number of applications submitted to Avant Money.
    - FinanceIrelandCount: Total number of applications submitted to Finance Ireland.
    - KBCCount: Total number of applications submitted to KBC.
    - OtherCount: Total number of applications submitted to lenders not specifically listed.
    - PermanentTSBCount: Total number of applications submitted to Permanent TSB.
    - UlsterCount: Total number of applications submitted to Ulster Bank.
    """
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
    """
    Counts number of days between date1 and date2

    Parameters:
    - date1 in format dd/mm/yyyy
    - date2 in format dd/mm/yyyy

    Returns:
    - number of days between date1 and date2
    """
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
    """
    Counts the amount of different mortgage types 

    Parameters:
    - clients (list): A list of client objects, where each object has an 'mortgage_type' attribute.

    Returns:
    - NewHomeCount the number of New Home mortgage applications
    - RemortgagingCount the number of Remortgaging mortgage applications
    """
    NewHomeCount = 0 
    RemortgagingCount = 0
    for client in clients:
        if client.mortgage_type == "Purchasing a New Home":
            NewHomeCount += 1
        elif client.mortgage_type == "Remortgaging Existing Loan":
            RemortgagingCount += 1
    return NewHomeCount, RemortgagingCount

def PropertyValue(clients):
    """
    Calculates the mean and standard deviation of the property values 

    Parameters:
    - clients (list): A list of client objects, where each object has an 'property_value' attribute.

    Returns:
    - mean, the average of all property values 
    - std_dev, the standard deviation of the property values 
    """
    values = []
    for client in clients:
        if client.property_value > 10000 and client.property_value < 30000000:
            values.append(client.property_value)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev    

def MortgageAmountProposed(clients):
    """
    Calculates the mean and standard deviation of the mortgage amount proposed

    Parameters:
    - clients (list): A list of client objects, where each object has an 'mortgage_amount_proposed' attribute.

    Returns:
    - mean, the average of all mortgage amounts proposed
    - std_dev, the standard deviation of the mortgage amounts proposed
    """
    values = []
    for client in clients:
        if client.mortgage_amount_proposed > 10000 and client.mortgage_amount_proposed < client.property_value:
            values.append(client.mortgage_amount_proposed)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev    

def Applications(clients):
    """
    Counts the total applications in the "application" status 

    Parameters:
    - clients (list): A list of client objects, where each object has an 'lead_status' attribute.

    Returns:
    - AppCount, the total number of application in the "application" status
    - len(clients)-AppCount, the number of applications not in the "application" status
    """
    AppCount = 0
    for client in clients:
        if client.lead_status=="Application":
            AppCount += 1
    return AppCount, len(clients)-AppCount

def InterestRateType(clients):
    """
    Counts the fixed and variable interest types

    Parameters:
    - clients (list): A list of client objects, where each object has an 'interest_rate_type' attribute.

    Returns:
    - FixedCount, the amount of "fixed" interest type
    - Variable, the amount of "variable" interest type
    """
    FixedCount = 0
    VariableCount = 0
    for client in clients:
        if client.interest_rate_type == "Fixed":
            FixedCount+=1
        elif client.interest_rate_type == "Variable":
            VariableCount+=1
    return FixedCount, VariableCount


def CurrentLender(clients):
    """
    Counts the number of applicants there are for all lenders

    Parameters:
    - clients (list): A list of client objects, where each object has an 'aip_lender_submitted_to' attribute.

    Returns:
    - AIBCount, the number of applicants whose current lender is AIB
    - HavenCount, the number of applicants whose current lender is Haven
    - BOICount, the number of applicants whose current lender is BOI
    - EBSCount, the number of applicants whose current lender is EBS
    - PepperCount, the number of applicants whose current lender is Pepper
    - KBCCount, the number of applicants whose current lender is KBC
    - PTSBCount, the number of applicants whose current lender is PTSB
    - UlsterCount, the number of applicants whose current lender is Ulster
    - BlankCount, the number of applicants whose current lender is blank
    """
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
    """
    Calculates the mean and standard deviation of the current interest rates

    Parameters:
    - clients (list): A list of client objects, where each object has an 'current_interest_rate' attribute.

    Returns:
    - mean, the mean of all current interest rates
    -std_dev, the standard deviation of all the current interest rates
    """
    values = []
    for client in clients:
        if client.current_interest_rate>0:
            values.append(client.current_interest_rate)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev  

def CurrentMonthlyPayments(clients):
    """
    Calculates the mean and standard deviation of the current monthly payments

    Parameters:
    - clients (list): A list of client objects, where each object has an 'current_monthly_payment' attribute.

    Returns:
    - mean, the mean of all current monthly payments
    - std_dev, the standard deviation of all the current monthly payments
    """
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
    """
    Calculates the mean and standard deviation of the gross basic income

    Parameters:
    - clients (list): A list of client objects, where each object has an 'lead_gross_basic_income' attribute.

    Returns:
    - mean, the mean of all gross basic income
    - std_dev, the standard deviation of all the gross basic income
    """
    values = []
    for client in clients:
        if client.lead_gross_basic_income>=25000:
            values.append(client.lead_gross_basic_income)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev  

def documentationUploaded(clients):
    """
    Calculates the mean and standard deviation of the primary documents percentage

    Parameters:
    - clients (list): A list of client objects, where each object has an 'primary_documents_percentage' attribute.

    Returns:
    - mean, the mean of all primary documents percentage
    - std_dev, the standard deviation of all the primary documents percentage
    """
    values = []
    for client in clients:
        if client.documents_uploaded:
            if client.primary_documents_percentage is not None:
                values.append(client.primary_documents_percentage)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev

def secondaryDocumentationUploaded(clients):
    """
    Calculates the mean and standard deviation of the secondary documents percentage

    Parameters:
    - clients (list): A list of client objects, where each object has an 'secondary_documents_percentage' attribute.

    Returns:
    - mean, the mean of all secondary documents percentage
    - std_dev, the standard deviation of all the secondary documents percentage
    """
    values = []
    for client in clients:
        if client.secondary_documents_upload:
            if not np.isnan(client.secondary_documents_percentage):
                values.append(client.primary_documents_percentage)
    mean = np.mean(values)
    std_dev = np.std(values)
    return mean, std_dev
