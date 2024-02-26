import numpy as np
# from Scripts.Timeline import calculate_differences

def getStage(applications, stageName):
    stageArray = []
    noneCount = 0
    for application in applications:
        if application[stageName] is not None:
            stageArray.append(application[stageName])
        else:
            noneCount += 1
    population = 1 - (noneCount/ (len(stageArray) + noneCount))
    return stageArray, round(population * 100, 2)

def stageAverageAndSD(applications, stage):
    stageArray, population = getStage(applications, stage)
    return np.mean(stageArray), np.std(stageArray), population

def rankForEachStage(applications, stage):
    stageArray, population = getStage(applications, stage)
    return sorted(stageArray), population

def WhatType(clients):
    FTBCount = 0
    STBCount = 0
    SwitchingCount = 0
    EquityCount = 0
    for client in clients:
        if client.type == "First Time Buyer":
            FTBCount += 1
        elif client.type == "Second Time Buyer":
            STBCount += 1
        elif client.type == "Switching":
            SwitchingCount += 1
        else:
            EquityCount += 1
    return FTBCount, STBCount, SwitchingCount, EquityCount

def SingleOrJoint(clients):
    singleCount = 0
    jointCount = 0
    for client in clients:
        if client.single_joint == "Single":
            singleCount += 1
        elif client.single_joint == "Joint":
            jointCount += 1
    return singleCount,jointCount

def WhatBank(clients):
    ICSCount = 0
    HavenCount = 0
    BOICount = 0
    OtherCount = 0
    for client in clients:
        if client.submitted_to == "ics":
            ICSCount += 1
        elif client.submitted_to == "haven":
            HavenCount += 1
        elif client.submitted_to == "boi":
            BOICount += 1
        else:
            OtherCount += 1
    return ICSCount,HavenCount,BOICount,OtherCount


# getStage:
#   Takes in an array of type Application and the stage of the application
#   we are looking for as a string. 
#   Returns an array of type integer with the durations of that stage for each application 
#   and a population expressed as a percentage that tells us how many applications are in that stage.

# def getStage(applications, stageName):
#     stageArray = []
#     noneCount = 0
#     for applicationTimeline in applications:
#         diffs = {}
#         # diffs = applicationTimeline.calculate_differences()
#         if diffs.get(stageName) is not None:
#            stageArray.append(diffs.get(stageName)) 
#         else:
#             noneCount += 1
#     population = 1 - (noneCount / (len(stageArray) + noneCount))
#     return stageArray, population

# def stageAverageAndSD(applications, stage):
#     stageArray, population = getStage(applications, stage)
#     return np.mean(stageArray), np.std(stageArray), population

# def rankForEachStage(applications, stage):
#     stageArray, population = getStage(applications, stage)
#     return sorted(stageArray), population

# def singleOrJointClient(clients):
#     for client in clients:
#         if 

# # def stoppingStage(applications):
# #     for application in applications:
# #         currentStage = getattr(application, c) # what is the exact name of this

# def stageForAgents(agents, stage):
    
#     return