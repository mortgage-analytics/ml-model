import pandas as pd
from Timeline import Timeline
from Client import Client
import data_analytics
import numpy as np


stagesNames = ["lead_to_application","application_to_aip_submission","aip_submission_to_response",
               "credit_submission_to_advisor_review","advisor_to_recommendation","recommendation_to_pack_submission",
               "pack_submission_to_offer_letter_received","offer_letter_to_loan_offer_completed","loan_offer_to_estimated_closing",
               "estimated_closing_to_closing","closing_to_agreed_drawdown","agreed_drawdown_to_funds_release",
               "funds_release_to_fixed_rate_maturity","fixed_rate_maturity_to_drawdown_completed","submission_to_loan_offer_expiry",
               "valuation_requested_to_received","contract_signed_to_deeds_with_solicitor"
               ]


if __name__ == "__main__":
    file_path = r"C:\Users\rober\OneDrive\Documents\College\AA-Sweng_repo_new\ml-model\data.csv"
    df = pd.read_csv(file_path)
    
    client_type = df["client_type"].tolist()
    application_type = df["application_type"].tolist()
    mortgage_type = df["mortgage_type"].tolist()
    property_value = df["property_value"].tolist()
    mortgage_amount_proposed = df["mortgage_amount_proposed"].tolist()
    existing_mortgage_balance = df["existing_mortgage_balance"].tolist()
    lead_created_date = df["lead_created_date"].tolist()
    lead_status = df["lead_status"].tolist()
    application_created_date = df["application_created_date"].tolist()
    modified_date = df["modified_date"].tolist()
    application_stage = df["application_stage"].tolist()
    application_status = df["application_status"].tolist()
    link_sent = df["link_sent"].tolist()
    documents_uploaded = df["documents_uploaded"].tolist()
    last_doc_upload = df["last_doc_upload"].tolist()
    aip_lender_submitted_to = df["aip_lender_submitted_to"].tolist()
    aip_submission_date = df["aip_submission_date"].tolist()
    aip_response_received = df["aip_response_received"].tolist()
    aip_expiration = df["aip_expiration"].tolist()
    aip_amount = df["aip_amount"].tolist()
    next_action_date = df["next_action_date"].tolist()
    primary_consent_granted = df["primary_consent_granted"].tolist()
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
    fact_find_surplus_per_month = df["fact_find_surplus_per_month"].tolist()
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
    drawdown_amount = df["drawdown_amount"].tolist()
    chosen_lender_product = df["chosen_lender_product"].tolist()
    sos_sent = df["sos_sent"].tolist()
    sos_signed = df["sos_signed"].tolist()
    interest_rate_type = df["interest_rate_type"].tolist()
    fixed_rate_term_needed = df["fixed_rate_term_needed"].tolist()
    valuation_expiry_date = df["valuation_expiry_date"].tolist()
    mortgage_term = df["mortgage_term"].tolist()
    submitted_to_lender_date = df["submitted_to_lender_date"].tolist()
    loan_offer_expiry_date = df["loan_offer_expiry_date"].tolist()
    valuation_requested_date = df["valuation_requested_date"].tolist()
    valuation_received_date = df["valuation_received_date"].tolist()
    passed_to_completions = df["passed_to_completions"].tolist()
    signed_contracts_received_date = df["signed_contracts_received_date"].tolist()
    title_deeds_with_solicitor_date = df["title_deeds_with_solicitor_date"].tolist()
    current_lender = df["current_lender"].tolist()
    term_remaining = df["term_remaining"].tolist()
    current_interest_rate = df["current_interest_rate"].tolist()
    current_monthly_payment = df["current_monthly_payment"].tolist()
    chosen_lender_provider = df["chosen_lender_provider"].tolist()
    loan_offer_requested = df["loan_offer_requested"].tolist()
    applicant_one_year_of_birth = df["applicant_one_year_of_birth"].tolist()
    applicant_two_year_of_birth = df["applicant_two_year_of_birth"].tolist()
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
        "lead_to_application": [],
        "application_to_aip_submission": [],
        "aip_submission_to_response": [],
        "credit_submission_to_advisor_review": [],
        "advisor_to_recommendation": [],
        "recommendation_to_pack_submission": [],
        "pack_submission_to_offer_letter_received": [],
        "offer_letter_to_loan_offer_completed": [],
        "loan_offer_to_estimated_closing": [],
        "estimated_closing_to_closing": [],
        "closing_to_agreed_drawdown": [],
        "agreed_drawdown_to_funds_release": [],
        "funds_release_to_fixed_rate_maturity": [],
        "fixed_rate_maturity_to_drawdown_completed": [],
        "submission_to_loan_offer_expiry": [],
        "valuation_requested_to_received": [],
        "contract_signed_to_deeds_with_solicitor": []
        }
    
    def calculate_total_income(lead_gross_basic_income, lead_other_guaranteed_income, lead_overtime, lead_bonus, lead_commission, lead_pension, lead_social_welfare, lead_maintenance_received, lead_other_variable_income):
        income_components = [lead_gross_basic_income, lead_other_guaranteed_income, lead_overtime, lead_bonus, lead_commission, lead_pension, lead_social_welfare, lead_maintenance_received, lead_other_variable_income, lead_other_guaranteed_income]
        income_components = [np.nan if x is None else x for x in income_components]
        total_income = np.nansum(income_components)
        return total_income

    clientsArray = []
    for i in range(0, len(lead_created_date)):
        sum_of_income = calculate_total_income(lead_gross_basic_income[i], lead_other_guaranteed_income[i], lead_overtime[i], lead_bonus[i], lead_commission[i], lead_pension[i], lead_social_welfare[i], lead_maintenance_received[i], lead_other_variable_income[i])
        client = Client(client_type[i], aip_lender_submitted_to[i], property_value[i], mortgage_amount_proposed[i],
                        application_type[i],mortgage_type[i],application_stage[i],application_status[i],documents_uploaded[i],
                        aip_amount[i],fact_find_surplus_per_month[i],sum_of_income, None)
        clientsArray.append(client)
        timeline = Timeline(lead_created_date[i], application_created_date[i], modified_date[i], aip_submission_date[i], 
                 aip_response_received[i], aip_expiration[i], last_doc_upload[i], next_action_date[i], 
                 advisor_review_completed_date[i], credit_submission_completed_date[i], recommendation_completed_date[i], 
                 pack_submitted_to_lender_date[i], offer_letter_received_date[i], loan_offer_completed_date[i], 
                 estimated_closing_date[i], closing_date[i], agreed_drawdown_date[i], funds_release_date[i], 
                 fixed_rate_maturity_date[i], drawdown_completed_date[i], submitted_to_lender_date[i], loan_offer_expiry_date[i], 
                 valuation_requested_date[i], valuation_received_date[i], signed_contracts_received_date[i], 
                 title_deeds_with_solicitor_date[i])
        applicationArray.append(timeline)
        ##diffsArray.append(timeline.calculate_differences())
        client.application = timeline
        ##client.display_info()
    
    for timeline in applicationArray:
        newDiffs = timeline.calculate_differences()
        for stageName, diff in newDiffs.items():
            diffsDictionary[stageName].append(diff)

    stats = Timeline.calculate_stats(diffsDictionary)
    for stage, values in stats.items():
        mean = values['average']
        std_dev = values['standard_deviation']
        mean_str = 'nan' if mean is None else f"{mean:.2f}"
        std_dev_str = 'nan' if std_dev is None else f"{std_dev:.2f}"
        print(f"Stage: {stage}, Mean: {mean_str}, Standard Deviation: {std_dev_str}")

    mean_income, std_dev_income, highest_income, lowest_income = data_analytics.IncomeOfCompletedMortgages(clientsArray)
    print(f"The average income for completed mortgages applications is €{mean_income:.2f}, the standard deviation is €{std_dev_income:.2f}")
    print(f"The income for completed mortages ranges from €{highest_income} at the highest to €{lowest_income} at the lowest")
    AIP_Expected_Count,AIP_Granted_Count,Closed_Count,InfoGathering_Count,LoanOfferRec_Count,Not_Proceeding_Count,OnHold_Count,PreCompletion_Count,PreLoanOffer_Count = data_analytics.WhatType(clientsArray)

    ICSCount,HavenCount,BOICount,AvantCount,FinanceIrelandCount,KBCCount,OtherCount,PermanentTSBCOunt,UlsterCount = data_analytics.WhatBank(clientsArray)

    singleCount,jointCount = data_analytics.SingleOrJoint(clientsArray)

    print(f"We have {singleCount} single clients and {jointCount} joint clients")
    print(f"We have {ICSCount} customers from ICS, {UlsterCount} customers from Ulster Bank,{PermanentTSBCOunt} customers from Permanent TSB, {KBCCount} customers from KBC, {FinanceIrelandCount} customers from Finance Ireland, {AvantCount} customers from Avant, {HavenCount} customers from Haven, {BOICount} customers from BOI and {OtherCount} from other banks")
    
    meanDaysToCompletion, stdDevDaysToCompletion = data_analytics.AverageTimeToCompletion(clientsArray)
    print(f"The mean amount of days to receive a loan offer is {meanDaysToCompletion}, with a standard deviation of {stdDevDaysToCompletion}")
