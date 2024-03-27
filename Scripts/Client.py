# from Timeline import Timeline

class Client:
    def __init__(self, client_type, aip_lender_submitted_to, property_value, mortgage_amount_proposed,
                  application_type, mortgage_type,application_stage,application_status,documents_uploaded,
                  aip_amount,fact_find_surplus_per_month,sum_of_income,application):
        self.client_type = client_type
        self.aip_lender_submitted_to = aip_lender_submitted_to
        self.property_value = property_value
        self.mortgage_amount_proposed = mortgage_amount_proposed
        self.application_type = application_type
        self.application = application
        self.mortgage_type = mortgage_type
        self.application_stage = application_stage
        self.application_status = application_status
        self.documents_uploaded = documents_uploaded
        self.aip_amount = aip_amount
        self.fact_find_surplus_per_month =fact_find_surplus_per_month
        self.sum_of_income = sum_of_income


    def display_info(self):
        """Prints the client's information."""
        print(f"Client Type: {self.client_type}")
        print(f"Submitted To: {self.aip_lender_submitted_to}")
        print(f"Property Value: {self.property_value}")
        print(f"Mortgage Amount Proposed: {self.mortgage_amount_proposed}")
        print(f"Application Status: {self.application_status}")
        print(f"Application")

