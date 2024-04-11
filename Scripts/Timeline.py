from datetime import datetime
import numpy as np

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
        self.valuation_requested_date = valuation_requested_date
        self.valuation_received_date = valuation_received_date
        
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

        return diffs

