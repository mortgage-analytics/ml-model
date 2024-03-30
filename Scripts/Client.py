# from Timeline import Timeline

class Client:
    def __init__(self, aip_lender_submitted_to, property_value, mortgage_amount_proposed,
                 application_type, mortgage_type,application_stage,application_status,documents_uploaded,
                 sum_of_income,current_interest_rate,current_monthly_payment,lead_gross_basic_income,lead_status,interest_rate_type,application):
        self.aip_lender_submitted_to = aip_lender_submitted_to
        self.property_value = property_value
        self.mortgage_amount_proposed = mortgage_amount_proposed
        self.application_type = application_type
        self.application = application
        self.mortgage_type = mortgage_type
        self.application_stage = application_stage
        self.application_status = application_status
        self.documents_uploaded = documents_uploaded
        self.sum_of_income = sum_of_income
        self.current_interest_rate = current_interest_rate
        self.current_monthly_payment = current_monthly_payment
        self.lead_gross_basic_income = lead_gross_basic_income
        self.lead_status = lead_status
        self.interest_rate_type = interest_rate_type

    def display_info(self):
        """Prints the client's information."""
        print(f"Client Type: {self.client_type}")
        print(f"Submitted To: {self.aip_lender_submitted_to}")
        print(f"Property Value: {self.property_value}")
        print(f"Mortgage Amount Proposed: {self.mortgage_amount_proposed}")
        print(f"Application Status: {self.application_status}")
        print(f"Application")

