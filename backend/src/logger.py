import logging
import sys

log = logging.getLogger('server-logger')
log.setLevel(logging.INFO)

logFormatter = logging.Formatter('> [%(asctime)s]-[%(levelname)s]: %(message)s')

consoleHandler = logging.StreamHandler(sys.stdout)
consoleHandler.setFormatter(logFormatter)
log.addHandler(consoleHandler)

