from datetime import datetime
import numpy as np
# from Client import Client

class Timeline:
    def __init__(self, lead_created_date, application_created_date, advisor_review_completion_date,
                 submission_date, response_date, valuation_received, loan_offer_received, completed_date, customer):
        # These are expected to be lists of date strings
        self.lead_created_date = lead_created_date
        self.application_created_date = application_created_date
        self.advisor_review_completion_date = advisor_review_completion_date
        self.submission_date = submission_date
        self.response_date = response_date
        self.valuation_received = valuation_received
        self.loan_offer_received = loan_offer_received
        self.completed_date = completed_date
        self.customer = customer

    def calculate_stats(self, diffs):
        stats = {}
        for key, value_list in diffs.items():
            filtered_values = []
            for value in value_list:
                if value is not None and value >= 0:
                    filtered_values.append(value)

            if len(filtered_values)>0:
                average = np.mean(filtered_values)
                std_dev = np.std(filtered_values)
            else:
                average = None
                std_dev = None

            stats[key] = {
                'average': average,
                'standard_deviation': std_dev
            }
        return stats



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
            'lead_to_app': self._num_of_days(self.lead_created_date, self.application_created_date),
            'app_to_advisor': self._num_of_days(self.application_created_date,self.advisor_review_completion_date),
            'advisor_to_submission': self._num_of_days(self.advisor_review_completion_date,self.submission_date),
            'submission_to_response': self._num_of_days(self.submission_date,self.response_date),
            'response_to_valuation': self._num_of_days(self.response_date, self.valuation_received),
            'valuation_to_loan_offer': self._num_of_days(self.valuation_received,self.loan_offer_received),
            'loan_offer_to_completed': self._num_of_days(self.loan_offer_received,self.completed_date)
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

