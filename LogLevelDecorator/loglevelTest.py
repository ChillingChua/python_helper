## example for testing ##
import logging
from LogLevelDecorator import logLevel

@logLevel(lvl='DEBUG')
def first():
    log.info('first on INFO level')
    log.debug('first on DEBUG level')
    log.warning('first on WARNING level')

@logLevel(lvl='WARNING')
def second():
    log.info('second on INFO level')
    log.debug('second on DEBUG level')
    log.warning('second on WARNING level')

log_level = getattr(logging, 'INFO', logging.INFO)
log_handler = logging.StreamHandler()
log = logging.getLogger('LogTest')
log.addHandler(log_handler)
log.setLevel(log_level)

first()
second()

