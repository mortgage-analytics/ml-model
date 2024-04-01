import pandas as pd
from Scripts.Timeline import Timeline
from Scripts.Client import Client
import data_analytics
import numpy as np


stagesNames = ["lead_to_application","application_to_aip_submission","aip_submission_to_response",
               "credit_submission_to_advisor_review","advisor_to_recommendation","recommendation_to_pack_submission",
               "pack_submission_to_offer_letter_received","offer_letter_to_loan_offer_completed","loan_offer_to_estimated_closing",
               "estimated_closing_to_closing","closing_to_agreed_drawdown","agreed_drawdown_to_funds_release",
               "funds_release_to_fixed_rate_maturity","fixed_rate_maturity_to_drawdown_completed","submission_to_loan_offer_expiry",
               "valuation_requested_to_received","contract_signed_to_deeds_with_solicitor"
               ]

def date():
    pass

def data_analytics():
    file_path = r"C:\Users\manue\Downloads\Data Analytics.csv"
    df = pd.read_csv(file_path)

   
    application_type = df["application_type"].tolist()
    mortgage_type = df["mortgage_type"].tolist()
    property_value = df["property_value"].tolist()
    mortgage_amount_proposed = df["mortgage_amount_proposed"].tolist()
    lead_created_date = df["lead_created_date"].tolist()
    lead_status = df["lead_status"].tolist()
    application_created_date = df["application_created_date"].tolist()
    application_stage = df["application_stage"].tolist()
    application_status = df["application_status"].tolist()
    documents_uploaded = df["documents_uploaded"].tolist()
    last_doc_upload = df["last_doc_upload"].tolist()
    aip_lender_submitted_to = df["aip_lender_submitted_to"].tolist()
    aip_submission_date = df["aip_submission_date"].tolist()
    aip_response_received = df["aip_response_received"].tolist()
    primary_personal_details_complete = df["primary_personal_details_complete"].tolist()
    primary_income_and_expenses_completed = df["primary_income_and_expenses_completed"].tolist()
    primary_assets_and_liabilities_completed = df["primary_assets_and_liabilities_completed"].tolist()
    primary_your_mortgage_completed = df["primary_your_mortgage_completed"].tolist()
    primary_tax_and_credit_checklist_completed = df["primary_tax_and_credit_checklist_completed"].tolist()
    primary_your_mortgage_needs_checklist_completed = df["primary_your_mortgage_needs_checklist_completed"].tolist()
    primary_document_upload_percent = df["primary_document_upload_percent"].tolist()
    secondary_consent_granted = df["secondary_consent_granted"].tolist()
    secondary_personal_details_completed = df["secondary_personal_details_completed"].tolist()
    secondary_income_and_expenses_completed = df["secondary_income_and_expenses_completed"].tolist()
    secondary_assets_and_liabilities_completed = df["secondary_assets_and_liabilities_completed"].tolist()
    secondary_your_mortgage_completed = df["secondary_your_mortgage_completed"].tolist()
    secondary_tax_and_credit_checklist_completed = df["secondary_tax_and_credit_checklist_completed"].tolist()
    secondary_your_mortgage_needs_checklist_completed = df["secondary_your_mortgage_needs_checklist_completed"].tolist()
    secondary_document_upload_percent = df["secondary_document_upload_percent"].tolist()
    advisor_review_completed_date = df["advisor_review_completed_date"].tolist()
    credit_submission_completed_date = df["credit_submission_completed_date"].tolist()
    recommendation_completed_date = df["recommendation_completed_date"].tolist()
    pack_submitted_to_lender_date = df["pack_submitted_to_lender_date"].tolist()
    offer_letter_received_date = df["offer_letter_received_date"].tolist()
    loan_offer_completed_date = df["loan_offer_completed_date"].tolist()
    estimated_closing_date = df["estimated_closing_date"].tolist()
    closing_date = df["closing_date"].tolist()
    agreed_drawdown_date = df["agreed_drawdown_date"].tolist()
    funds_release_date = df["funds_release_date"].tolist()
    fixed_rate_maturity_date = df["fixed_rate_maturity_date"].tolist()
    drawdown_completed_date = df["drawdown_completed_date"].tolist()
    interest_rate_type = df["interest_rate_type"].tolist()
    submitted_to_lender_date = df["submitted_to_lender_date"].tolist()
    valuation_requested_date = df["valuation_requested_date"].tolist()
    valuation_received_date = df["valuation_received_date"].tolist()
    passed_to_completions = df["passed_to_completions"].tolist()
    signed_contracts_received_date = df["signed_contracts_received_date"].tolist()
    title_deeds_with_solicitor_date = df["title_deeds_with_solicitor_date"].tolist()
    current_lender = df["current_lender"].tolist()
    current_interest_rate = df["current_interest_rate"].tolist()
    current_monthly_payment = df["current_monthly_payment"].tolist()
    chosen_lender_provider = df["chosen_lender_provider"].tolist()
    loan_offer_requested = df["loan_offer_requested"].tolist()
    lead_gross_basic_income = df["lead_gross_basic_income"].tolist()
    lead_other_guaranteed_income = df["lead_other_guaranteed_income"].tolist()
    lead_overtime = df["lead_overtime"].tolist()
    lead_bonus = df["lead_bonus"].tolist()
    lead_commission = df["lead_commission"].tolist()
    lead_pension = df["lead_pension"].tolist()
    lead_social_welfare = df["lead_social_welfare"].tolist()
    lead_maintenance_received = df["lead_maintenance_received"].tolist()
    lead_other_variable_income = df["lead_other_variable_income"].tolist()
    



    applicationArray = []
    diffsDictionary = {
        "lead_to_application" : [],
        "application_to_last_doc" : [],
        "last_doc_to_aip_submission" : [],
        "aip_submission_to_response" : [],
        "aip_response_to_advisor_review" : [],
        "advisor_review_to_credit_submission" : [],
        "credit_submission_to_recommendation" : [],
        "recommendation_to_pack_submitted_to_lender" : [],
        "pack_submitted_to_offer_letter_received" : [],
        "offer_letter_received_to_loan_offer_completed" : [], 
        "loan_offer_completed_to_closing_date" : [],
        "valuation_requested_to_valuation_received" : [],
        "estimated_to_closing_date" : []
        }
    
    def calculate_total_income(lead_gross_basic_income, lead_other_guaranteed_income, lead_overtime, lead_bonus, lead_commission, lead_pension, lead_social_welfare, lead_maintenance_received, lead_other_variable_income):
        income_components = [lead_gross_basic_income, lead_other_guaranteed_income, lead_overtime, lead_bonus, lead_commission, lead_pension, lead_social_welfare, lead_maintenance_received, lead_other_variable_income, lead_other_guaranteed_income]
        income_components = [np.nan if x is None else x for x in income_components]
        total_income = np.nansum(income_components)
        return total_income
    
    def secondary(consent, personal_details, income, assets, your_mortgage, tax, needs):
        if consent and personal_details and income and assets and your_mortgage and tax and needs:
            return True
        else:
            return False

    clientsArray = []
    # diffsArray = []
    for i in range(0, len(lead_created_date)):
        secondary_document_upload = secondary(secondary_consent_granted, secondary_personal_details_completed, secondary_income_and_expenses_completed,
            secondary_assets_and_liabilities_completed, secondary_your_mortgage_completed, secondary_tax_and_credit_checklist_completed, secondary_your_mortgage_needs_checklist_completed)
        sum_of_income = calculate_total_income(lead_gross_basic_income[i], lead_other_guaranteed_income[i], lead_overtime[i], lead_bonus[i], lead_commission[i], lead_pension[i], lead_social_welfare[i], lead_maintenance_received[i], lead_other_variable_income[i])
        client = Client(aip_lender_submitted_to[i], property_value[i], mortgage_amount_proposed[i],
                        application_type[i],mortgage_type[i],application_stage[i],application_status[i],documents_uploaded[i], primary_document_upload_percent[i],
                        secondary_document_upload, secondary_document_upload_percent[i],
                        sum_of_income,current_interest_rate[i],current_monthly_payment[i],lead_gross_basic_income[i],lead_status[i],interest_rate_type[i], None)
        clientsArray.append(client)
        # timeline = Timeline(lead_created_date[i], application_created_date[i], aip_submission_date[i], 
        #          aip_response_received[i], last_doc_upload[i],advisor_review_completed_date[i], credit_submission_completed_date[i], recommendation_completed_date[i], 
        #          pack_submitted_to_lender_date[i], offer_letter_received_date[i], loan_offer_completed_date[i], 
        #          estimated_closing_date[i], closing_date[i], agreed_drawdown_date[i], funds_release_date[i], 
        #          fixed_rate_maturity_date[i], drawdown_completed_date[i], submitted_to_lender_date[i], 
        #          valuation_requested_date[i], valuation_received_date[i], signed_contracts_received_date[i], 
        #          title_deeds_with_solicitor_date[i])
        
        timeline = Timeline(lead_created_date[i],application_created_date[i], aip_submission_date[i],
                            aip_response_received[i], last_doc_upload[i], advisor_review_completed_date[i], credit_submission_completed_date[i],
                            recommendation_completed_date[i], pack_submitted_to_lender_date[i], offer_letter_received_date[i],
                            loan_offer_completed_date[i], estimated_closing_date[i], closing_date[i], valuation_requested_date[i],
                            valuation_received_date[i])
        applicationArray.append(timeline)
        # diffsArray.append(timeline.calculate_differences())
        client.application = timeline
        ##client.display_info()
    
    for timeline in applicationArray:
        newDiffs = timeline.calculate_differences()
        for stageName, diff in newDiffs.items():
            diffsDictionary[stageName].append(diff)

    stats = Timeline.calculate_stats(diffsDictionary)
    dictionaryToReturn = {}
    for stage, values in stats.items():
        mean = values['average']
        std_dev = values['standard_deviation']
        biggest = values['top_5_biggest']
        smallest = values['top_5_smallest']
        mean_str = 'nan' if mean is None else f"{mean:.2f}"
        std_dev_str = 'nan' if std_dev is None else f"{std_dev:.2f}"
        dictionaryToReturn[stage] = [mean, std_dev, biggest, smallest]
        print(f"Stage: {stage}, Mean: {mean_str}, Standard Deviation: {std_dev_str}, with the biggest values being {biggest}" +
              f" and the smallest being {smallest}")

    dictionaryToReturn['mean_income'], dictionaryToReturn['std_dev_income'], dictionaryToReturn['highest_income'], dictionaryToReturn['lowest_income'] = data_analytics.IncomeOfCompletedMortgages(clientsArray)
 
    dictionaryToReturn['AIP_Expected_Count'], dictionaryToReturn['AIP_Granted_Count'], dictionaryToReturn['Closed_Count'], dictionaryToReturn['InfoGathering_Count'], dictionaryToReturn['LoanOfferRec_Count'], dictionaryToReturn['Not_Proceeding_Count'], dictionaryToReturn['OnHold_Count'], dictionaryToReturn['PreCompletion_Count'], dictionaryToReturn['PreLoanOffer_Count'] = data_analytics.WhatType(clientsArray)

    dictionaryToReturn['ICSCount1'], dictionaryToReturn['HavenCount1'], dictionaryToReturn['BOICount1'], dictionaryToReturn['AvantCount1'], dictionaryToReturn['FinanceIrelandCount1'], dictionaryToReturn['KBCCount1'], dictionaryToReturn['OtherCount1'], dictionaryToReturn['PermanentTSBCOunt1'], dictionaryToReturn['UlsterCount1'] = data_analytics.WhatBank(clientsArray)

    dictionaryToReturn['AIBCount2'], dictionaryToReturn['HavenCount2'], dictionaryToReturn['BOICount2'], dictionaryToReturn['EBSCount2'], dictionaryToReturn['PepperCount2'], dictionaryToReturn['KBCCount2'], dictionaryToReturn['BlankCount2'], dictionaryToReturn['PTSBCount2'], dictionaryToReturn['UlsterCount2'] = data_analytics.CurrentLender(clientsArray)

    dictionaryToReturn['ICSCount3'], dictionaryToReturn['HavenCount3'], dictionaryToReturn['AvantCount3'], dictionaryToReturn['MortgageStoreCount3'], dictionaryToReturn['PermanentTSBCount3'], dictionaryToReturn['BlankCount3'] = data_analytics.ChosenLenderProvider(clientsArray)

    dictionaryToReturn['NewHomeCount'], dictionaryToReturn['RemortgagingCount'] = data_analytics.MortgageType(clientsArray)

    dictionaryToReturn['mean_PropertyValue'], dictionaryToReturn['std_dev_PropertyValue'] = data_analytics.PropertyValue(clientsArray)

    dictionaryToReturn['mean_InterestRate'], dictionaryToReturn['std_dev_InterestRate'] = data_analytics.CurrentInterestRate(clientsArray)

    dictionaryToReturn['mean_MonthlyPayments'], dictionaryToReturn['std_dev_MonthlyPayments'] = data_analytics.CurrentMonthlyPayments(clientsArray)

    dictionaryToReturn['mean_GrossIncome'], dictionaryToReturn['std_dev_GrossIncome'] = data_analytics.GrossBasicIncome(clientsArray)

    dictionaryToReturn['mean_MortgageAmountProposed'], dictionaryToReturn['std_dev_MortgageAmountProposed'] = data_analytics.MortgageAmountProposed(clientsArray)

    dictionaryToReturn['ApplicationsCount'], dictionaryToReturn['others'] = data_analytics.Applications(clientsArray)

    dictionaryToReturn['FixedInterestRateCount'], dictionaryToReturn['VariableInterestRateCount'] = data_analytics.InterestRateType(clientsArray)

    dictionaryToReturn['meanDaysToCompletion'], dictionaryToReturn['stdDevDaysToCompletion'] = data_analytics.AverageTimeToCompletion(clientsArray)

    dictionaryToReturn['singleCount'], dictionaryToReturn['jointCount'] = data_analytics.SingleOrJoint(clientsArray)
    
    dictionaryToReturn['meanDocUpload'], dictionaryToReturn['stdDocUpload'] = data_analytics.documentationUploaded(clientsArray)
    
    dictionaryToReturn['meanSecDocUpload'], dictionaryToReturn['stdSecDocUpload'] = data_analytics.secondaryDocumentationUploaded(clientsArray)


    # print(f"The average income for completed mortgages applications is €{mean_income:.2f}, the standard deviation is €{std_dev_income:.2f}")
    
    # print(f"The income for completed mortages ranges from €{highest_income} at the highest to €{lowest_income} at the lowest")

    # print(f"We have {singleCount} single clients and {jointCount} joint clients")

    # print(f"We have {ICSCount1} customers from ICS, {UlsterCount1} customers from Ulster Bank,{PermanentTSBCOunt1} customers from Permanent TSB, {KBCCount1} customers from KBC, {FinanceIrelandCount1} customers from Finance Ireland, {AvantCount1} customers from Avant, {HavenCount1} customers from Haven, {BOICount1} customers from BOI and {OtherCount1} from other banks")

    # print(f"The mean amount of days to receive a loan offer is {meanDaysToCompletion}, with a standard deviation of {stdDevDaysToCompletion}")

    # print(f"The total number of new home mortgage applications is {NewHomeCount}, and the total number of remortgaging applications is {RemortgagingCount}.")

    # print(f"The average property value in the applications is €{mean_PropertyValue:.2f}, with a standard deviation of €{std_dev_PropertyValue:.2f}.")

    # print(f"The average interest rate for current mortgages is {mean_InterestRate:.2f}%, with a standard deviation of {std_dev_InterestRate:.2f}%.")

    # print(f"The average monthly payment for current mortgages is €{mean_MonthlyPayments:.2f}, with a standard deviation of €{std_dev_MonthlyPayments:.2f}.")

    # print(f"The average gross income of applicants is €{mean_GrossIncome:.2f}, with a standard deviation of €{std_dev_GrossIncome:.2f}.")

    # print(f"The average proposed mortgage amount is €{mean_MortgageAmountProposed:.2f}, with a standard deviation of €{std_dev_MortgageAmountProposed:.2f}.")

    # print(f"The total number of mortgage applications is {ApplicationsCount}.")

    # print(f"There are {FixedInterestRateCount} applications with fixed interest rates and {VariableInterestRateCount} applications with variable interest rates.")
    
    # print(f"The average percentage of primary documents uploaded is {meanDocUpload:.2f}% and the standard deviation is {stdDocUpload:.2f}%")
    
    # print(f"The average percentage of secondary documents uploaded is {meanSecDocUpload:.2f}% and the standard deviation is {stdSecDocUpload:.2f}%")
    
    print(dictionaryToReturn)
    
    return dictionaryToReturn 
