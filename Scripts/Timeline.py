from datetime import datetime
import numpy as np
# from Client import Client

class Timeline:
    def __init__(self, lead_created_date, application_created_date, aip_submission_date, 
                 aip_response_received, last_doc_upload,advisor_review_completed_date, credit_submission_completed_date, recommendation_completed_date, 
                 pack_submitted_to_lender_date, offer_letter_received_date, loan_offer_completed_date, 
                 estimated_closing_date, closing_date, valuation_requested_date, valuation_received_date):
        self.lead_created_date = lead_created_date
        self.application_created_date = application_created_date
        self.aip_submission_date = aip_submission_date
        self.aip_response_received = aip_response_received
        self.last_doc_upload = last_doc_upload
        self.advisor_review_completed_date = advisor_review_completed_date
        self.credit_submission_completed_date = credit_submission_completed_date
        self.recommendation_completed_date = recommendation_completed_date
        self.pack_submitted_to_lender_date = pack_submitted_to_lender_date
        self.offer_letter_received_date = offer_letter_received_date
        self.loan_offer_completed_date = loan_offer_completed_date
        self.estimated_closing_date = estimated_closing_date
        self.closing_date = closing_date
        # self.agreed_drawdown_date = agreed_drawdown_date
        # self.funds_release_date = funds_release_date
        # self.fixed_rate_maturity_date = fixed_rate_maturity_date
        # self.drawdown_completed_date = drawdown_completed_date
        # self.submitted_to_lender_date = submitted_to_lender_date
        self.valuation_requested_date = valuation_requested_date
        self.valuation_received_date = valuation_received_date
        # self.signed_contracts_received_date = signed_contracts_received_date
        # self.title_deeds_with_solicitor_date = title_deeds_with_solicitor_date

        
    def calculate_stats(diffs):
        stats = {}
        for key, value_list in diffs.items():
            filtered_values = []
            for value in value_list:
                if value is not None and value >= 0:
                    filtered_values.append(value)

            if len(filtered_values)>0:
                average = np.mean(filtered_values)
                std_dev = np.std(filtered_values)
                sorted_values = sorted(filtered_values, reverse=True)

            else:
                average = None
                std_dev = None
            stats[key] = {
                'average': average,
                'standard_deviation': std_dev,
                'top_5_biggest' : sorted_values[:5],
                'top_5_smallest' : sorted_values[-5:]
            }
        return stats



    def _num_of_days(self, date1, date2):
        date_format = "%d/%m/%Y"  # Adjust the format as per your data
        # Check if either date is not a string (e.g., NaN represented as float or None)
        if not isinstance(date1, str) or not isinstance(date2, str):
            return None  # Or handle as appropriate for your application

        try:
            a = datetime.strptime(date1, date_format)
            b = datetime.strptime(date2, date_format)
            return (b - a).days
        except ValueError:
            print("got here third")
            # Handle the case where date parsing fails
            return None

    def calculate_differences(self):
        # Initialize lists to store the differences
        # diffs = {
        #     "lead_to_application": self._num_of_days(self.lead_created_date, self.application_created_date),
        #     "application_to_aip_submission": self._num_of_days(self.modified_date, self.application_created_date),
        #     "aip_submission_to_response": self._num_of_days(self.aip_response_received, self.aip_submission_date),
        #     "credit_submission_to_advisor_review": self._num_of_days(self.advisor_review_completed_date, self.credit_submission_completed_date),
        #     "advisor_to_recommendation": self._num_of_days(self.recommendation_completed_date, self.advisor_review_completed_date),
        #     "recommendation_to_pack_submission": self._num_of_days(self.pack_submitted_to_lender_date, self.recommendation_completed_date),
        #     "pack_submission_to_offer_letter_received": self._num_of_days(self.offer_letter_received_date, self.pack_submitted_to_lender_date),
        #     "offer_letter_to_loan_offer_completed": self._num_of_days(self.loan_offer_completed_date, self.offer_letter_received_date),
        #     "loan_offer_to_estimated_closing": self._num_of_days(self.estimated_closing_date, self.loan_offer_completed_date),
        #     "estimated_closing_to_closing": self._num_of_days(self.closing_date, self.estimated_closing_date),
        #     "closing_to_agreed_drawdown": self._num_of_days(self.agreed_drawdown_date, self.closing_date),
        #     "agreed_drawdown_to_funds_release": self._num_of_days(self.funds_release_date, self.agreed_drawdown_date),
        #     "funds_release_to_fixed_rate_maturity": self._num_of_days(self.fixed_rate_maturity_date, self.funds_release_date) if self.fixed_rate_maturity_date and self.funds_release_date else None,
        #     "fixed_rate_maturity_to_drawdown_completed": self._num_of_days(self.drawdown_completed_date, self.fixed_rate_maturity_date) if self.fixed_rate_maturity_date and self.drawdown_completed_date else None,
        #     "submission_to_loan_offer_expiry": self._num_of_days(self.loan_offer_expiry_date, self.submitted_to_lender_date),
        #     "valuation_requested_to_received": self._num_of_days(self.valuation_received_date, self.valuation_requested_date),
        #     "contract_signed_to_deeds_with_solicitor": self._num_of_days(self.title_deeds_with_solicitor_date, self.signed_contracts_received_date) if self.title_deeds_with_solicitor_date and self.signed_contracts_received_date else None,
        # }
        
        # print(self.lead_created_date)
        
        diffs = {
            "lead_to_application" : self._num_of_days(self.lead_created_date, self.application_created_date),
            "application_to_last_doc" : self._num_of_days(self.application_created_date, self.last_doc_upload),
            "last_doc_to_aip_submission" : self._num_of_days(self.last_doc_upload, self.aip_submission_date),
            "aip_submission_to_response" : self._num_of_days(self.aip_submission_date, self.aip_response_received),
            "aip_response_to_advisor_review" : self._num_of_days(self.aip_response_received, self.advisor_review_completed_date),
            "advisor_review_to_credit_submission" : self._num_of_days(self.advisor_review_completed_date, self.credit_submission_completed_date),
            "credit_submission_to_recommendation" : self._num_of_days(self.credit_submission_completed_date, self.recommendation_completed_date),
            "recommendation_to_pack_submitted_to_lender" : self._num_of_days(self.recommendation_completed_date, self.pack_submitted_to_lender_date),
            "pack_submitted_to_offer_letter_received" : self._num_of_days(self.pack_submitted_to_lender_date, self.offer_letter_received_date),
            "offer_letter_received_to_loan_offer_completed" : self._num_of_days(self.offer_letter_received_date, self.loan_offer_completed_date),
            "loan_offer_completed_to_closing_date" : self._num_of_days(self.loan_offer_completed_date, self.closing_date),
            "valuation_requested_to_valuation_received" : self._num_of_days(self.valuation_requested_date, self.valuation_received_date),
            "estimated_to_closing_date" : self._num_of_days(self.estimated_closing_date, self.closing_date)
        }

        # Iterate through the date arrays and calculate differences
        # for i in range(len(self.lead_created_date)):
        #     if i < len(self.application_created_date):
        #         diffs['lead_to_app'].append(self._num_of_days(self.lead_created_date[i], self.application_created_date[i]))
        #     if i < len(self.advisor_review_completion_date):
        #         diffs['app_to_advisor'].append(self._num_of_days(self.application_created_date[i], self.advisor_review_completion_date[i]))
        #     if i < len(self.submission_date):
        #         diffs['advisor_to_submission'].append(self._num_of_days(self.advisor_review_completion_date[i], self.submission_date[i]))
        #     if i < len(self.response_date):
        #         diffs['submission_to_response'].append(self._num_of_days(self.submission_date[i], self.response_date[i]))
        #     if i < len(self.valuation_received):
        #         diffs['response_to_valuation'].append(self._num_of_days(self.response_date[i], self.valuation_received[i]))
        #     if i < len(self.loan_offer_received):
        #         diffs['valuation_to_loan_offer'].append(self._num_of_days(self.valuation_received[i], self.loan_offer_received[i]))
        #     if i < len(self.completed_date):
        #         diffs['loan_offer_to_completed'].append(self._num_of_days(self.loan_offer_received[i], self.completed_date[i]))
        #
        return diffs

    def getStage(applications, stageName):
        stageArray = []
        noneCount=0
        for application in applications:
            if application[stageName] is not None:
                stageArray.append(application[stageName])
            else:
                noneCount += 1
        population = 1 - (noneCount/ (len(stageArray)+noneCount))
        return stageArray, population

    def stageAverageAndSD(applications, stage):
        stageArray, population = getStage(applications, stage)
        return np.mean(stageArray),np.std(stageArray),population

    def rankForEachStage(applications, stage):
        stageArray, population = getStage(applications, stage)
        return sorted(stageArray), population

