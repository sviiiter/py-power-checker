import logging.handlers
import sys
from config import app_env


loggers = []
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
loggers.append(planActivitiesLogger)

# out-of-regulations-activities definitions
outOfRegulationsActivitiesLogger = logging.getLogger("out-of-regulations-activities")
outOfRegulationsActivitiesLogger.setLevel(logging.DEBUG)

fileHandler = logging.handlers.RotatingFileHandler('runtime/logs/out_of_regulations_activities.log', maxBytes=300, backupCount=5)
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

outOfRegulationsActivitiesLogger.addHandler(fileHandler)
loggers.append(outOfRegulationsActivitiesLogger)

# accident-activities definitions
accidentActivitiesLogger = logging.getLogger("accident-activities")
accidentActivitiesLogger.setLevel(logging.DEBUG)

fileHandler = logging.handlers.RotatingFileHandler('runtime/logs/accident_activities.log', maxBytes=300, backupCount=5)
fileHandler.setLevel(logging.INFO)
fileHandler.setFormatter(formatter)

accidentActivitiesLogger.addHandler(fileHandler)
loggers.append(accidentActivitiesLogger)

debugLogger = logging.getLogger("debug-logger")
debugLogger.setLevel(logging.DEBUG)
loggers.append(debugLogger)

if app_env == 'debug':
    for l in loggers:
        l.addHandler(stdoutHandler)
