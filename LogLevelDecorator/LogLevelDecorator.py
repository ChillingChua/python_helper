__all__ = ['logLevel']

import inspect
import logging

class LogLevelDecorator(object):

    def __init__(self, f, log_lvl):
        self.f = f
        self.log_lvl = log_lvl

    def __call__(self):
        frm = inspect.stack()[-1]
        mod = inspect.getmodule(frm[0])
        old_log_lvl = mod.log.getEffectiveLevel()
        new_log_lvl = getattr(logging, self.log_lvl, 'WARNING')
        mod.log.setLevel(new_log_lvl)
        self.f()
        mod.log.setLevel(old_log_lvl)

def logLevel(function=None, lvl='INFO'):
    """
        import this definition to use the decorator

        @logLevel(lvl='DEBUG')
        def first():
            log.info('first on INFO level')
            log.debug('first on DEBUG level')
            log.warning('first on WARNING level')

        prints WARNING and DEBUG lines, but not the INFO
    """
    if function:
        return LogLevelDecorator(function)
    else:
        def _wrapper(function):
            return LogLevelDecorator(function, lvl)
        return _wrapper

