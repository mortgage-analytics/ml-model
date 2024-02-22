from datetime import datetime

class Timeline:
    def __init__(self, lead_created_date, application_created_date, advisor_review_completion_date,
                 submission_date, response_date, valuation_received, loan_offer_received, completed_date):
        # These are expected to be lists of date strings
        self.lead_created_date = lead_created_date
        self.application_created_date = application_created_date
        self.advisor_review_completion_date = advisor_review_completion_date
        self.submission_date = submission_date
        self.response_date = response_date
        self.valuation_received = valuation_received
        self.loan_offer_received = loan_offer_received
        self.completed_date = completed_date

    def _num_of_days(self, date1, date2):
        date_format = "%d-%m-%Y"  # Adjust the format as per your data
        # Check if either date is not a string (e.g., NaN represented as float or None)
        if not isinstance(date1, str) or not isinstance(date2, str):
            return None  # Or handle as appropriate for your application

        try:
            a = datetime.strptime(date1, date_format)
            b = datetime.strptime(date2, date_format)
            return (b - a).days
        except ValueError:
            # Handle the case where date parsing fails
            return None

    def calculate_differences(self):
        # Initialize lists to store the differences
        diffs = {
            'lead_to_app': [],
            'app_to_advisor': [],
            'advisor_to_submission': [],
            'submission_to_response': [],
            'response_to_valuation': [],
            'valuation_to_loan_offer': [],
            'loan_offer_to_completed': []
        }

        # Iterate through the date arrays and calculate differences
        for i in range(len(self.lead_created_date)):
            if i < len(self.application_created_date):
                diffs['lead_to_app'].append(self._num_of_days(self.lead_created_date[i], self.application_created_date[i]))
            if i < len(self.advisor_review_completion_date):
                diffs['app_to_advisor'].append(self._num_of_days(self.application_created_date[i], self.advisor_review_completion_date[i]))
            if i < len(self.submission_date):
                diffs['advisor_to_submission'].append(self._num_of_days(self.advisor_review_completion_date[i], self.submission_date[i]))
            if i < len(self.response_date):
                diffs['submission_to_response'].append(self._num_of_days(self.submission_date[i], self.response_date[i]))
            if i < len(self.valuation_received):
                diffs['response_to_valuation'].append(self._num_of_days(self.response_date[i], self.valuation_received[i]))
            if i < len(self.loan_offer_received):
                diffs['valuation_to_loan_offer'].append(self._num_of_days(self.valuation_received[i], self.loan_offer_received[i]))
            if i < len(self.completed_date):
                diffs['loan_offer_to_completed'].append(self._num_of_days(self.loan_offer_received[i], self.completed_date[i]))

        return diffs
