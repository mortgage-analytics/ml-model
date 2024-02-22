import numpy as np
# from Scripts.Timeline import calculate_differences

# getStage:
#   Takes in an array of type Application and the stage of the application
#   we are looking for as a string. 
#   Returns an array of type integer with the durations of that stage for each application 
#   and a population expressed as a percentage that tells us how many applications are in that stage.

def getStage(applications, stageName):
    stageArray = []
    noneCount = 0
    for applicationTimeline in applications:
        diffs = {}
        # diffs = applicationTimeline.calculate_differences()
        if diffs.get(stageName) is not None:
           stageArray.append(diffs.get(stageName)) 
        else:
            noneCount += 1
    population = 1 - (noneCount / (len(stageArray) + noneCount))
    return stageArray, population

def stageAverageAndSD(applications, stage):
    stageArray, population = getStage(applications, stage)
    return np.mean(stageArray), np.std(stageArray), population

def rankForEachStage(applications, stage):
    stageArray, population = getStage(applications, stage)
    return sorted(stageArray), population

# def stoppingStage(applications):
#     for application in applications:
#         currentStage = getattr(application, c) # what is the exact name of this