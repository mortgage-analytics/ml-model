# from Timeline import Timeline

class Client:
    def __init__(self, type, submitted_to, property_identification, mortgage_amount, single_joint, application):
        self.type = type
        self.submitted_to = submitted_to
        self.property_identification = property_identification
        self.mortgage_amount = mortgage_amount
        self.single_joint = single_joint
        self.application = application

    def display_info(self):
        """Prints the client's information."""
        print(f"Client Type: {self.type}")
        print(f"Submitted To: {self.submitted_to}")
        print(f"Property Identification: {self.property_identification}")
        print(f"Mortgage Amount: {self.mortgage_amount}")
        print(f"Application")

