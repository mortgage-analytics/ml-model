class Client:
    def __init__(self, type, submitted_to, property_identification, mortgage_amount, single_joint):
        self.type = type
        self.submitted_to = submitted_to
        self.property_identification = property_identification
        self.mortgage_amount = mortgage_amount
        self.single_joint = single_joint

    def display_info(self):
        """Prints the client's information."""
        print(f"Client Type: {self.type}")
        print(f"Submitted To: {self.submitted_to}")
        print(f"Property Identification: {self.property_identification}")
        print(f"Mortgage Amount: {self.mortgage_amount}")



    def WhatType(self,clients):
        FTBCount =0
        STBCount =0
        SwitchingCount=0
        EquityCount=0
        for client in clients:
            if client.type=="First Time Buyer":
                FTBCount+=1
            elif client.type== "Second Time Buyer":
                STBCount+=1
            elif client.type=="Switching":
                SwitchingCount+=1
            else:
                EquityCount+=1
        return FTBCount,STBCount,SwitchingCount,EquityCount

    def SingleOrJoint(self,clients):
        singleCount = 0
        jointCount = 0
        for client in clients:
            if client.single_joint == "Single":
                singleCount += 1
            elif client.single_joint == "Joint":
                jointCount += 1

        return singleCount,jointCount

    def WhatBank(self,clients):
        ICSCount =0
        HavenCount =0
        BOICount=0
        OtherCount=0
        for client in clients:
            if client.submitted_to=="ics":
                ICSCount+=1
            elif client.submitted_to== "haven":
                HavenCount+=1
            elif client.submitted_to=="boi":
                BOICount+=1
            else:
                OtherCount+=1
        return ICSCount,HavenCount,BOICount,OtherCount



