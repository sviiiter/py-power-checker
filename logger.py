import logging.handlers
import sys


formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

stdoutHandler = logging.StreamHandler(sys.stdout)
stdoutHandler.setLevel(logging.DEBUG)
stdoutHandler.setFormatter(formatter)

# plan-activities definitions
planActivitiesLogger = logging.getLogger("plan-activities")
planActivitiesLogger.setLevel(logging.DEBUG)

fileHandler = logging.handlers.RotatingFileHandler('runtime/logs/plan_activities.log', maxBytes=300, backupCount=5)
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

planActivitiesLogger.addHandler(fileHandler)
planActivitiesLogger.addHandler(stdoutHandler)

# out-of-regulations-activities definitions
outOfRegulationsActivitiesLogger = logging.getLogger("out-of-regulations-activities")
outOfRegulationsActivitiesLogger.setLevel(logging.DEBUG)

fileHandler = logging.handlers.RotatingFileHandler('runtime/logs/out_of_regulations_activities.log', maxBytes=300, backupCount=5)
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

outOfRegulationsActivitiesLogger.addHandler(fileHandler)
outOfRegulationsActivitiesLogger.addHandler(stdoutHandler)

# accident-activities definitions
accidentActivitiesLogger = logging.getLogger("accident-activities")
accidentActivitiesLogger.setLevel(logging.DEBUG)

fileHandler = logging.handlers.RotatingFileHandler('runtime/logs/accident_activities.log', maxBytes=300, backupCount=5)
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

accidentActivitiesLogger.addHandler(fileHandler)
accidentActivitiesLogger.addHandler(stdoutHandler)

