import logging
import sys
import definitions

log = logging.getLogger('server-logger')
log.setLevel(logging.INFO)

logFormatter = logging.Formatter('> [%(asctime)s]-[%(levelname)s]: %(message)s')

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logFormatter)
log.addHandler(consoleHandler)

logFilesPath = definitions.get_project_root() / 'logs' / 'log.txt'
fileHandler = logging.FileHandler(logFilesPath)
fileHandler.setFormatter(logFormatter)
log.addHandler(fileHandler)

