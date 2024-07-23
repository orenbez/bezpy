# ======================================================================================================================
# The 'retry' decorator
# ======================================================================================================================
# requires 'pip install retry'  0.9.2 latest version
# Documentation: https://pypi.org/project/retry/
# ======================================================================================================================
# As of June 2016, the retrying package is no longer being maintained.
# Consider using the active fork github.com/jd/tenacity, or alternatively github.com/litl/backoff.
# ======================================================================================================================
# Default Parameters: exceptions=Exception, tries=-1, delay=0, max_delay=None, backoff=1, jitter=0, logger=logging_logger

    # :param exceptions: an exception or a tuple of exceptions to catch. default: Exception.
    # :param tries: the maximum number of attempts. default: -1 (infinite).
    # :param delay: initial delay between attempts. default: 0.
    # :param max_delay: the maximum value of delay. default: None (no limit).
    # :param backoff: multiplier applied to delay between attempts. default: 1 (no backoff).
    # :param jitter: extra seconds added to delay between attempts. default: 0.
    #                fixed if a number, random if a range tuple (min, max)
    # :param logger: logger.warning(fmt, error, delay) will be called on failed attempts.
    #                default: retry.logging_logger. if None, logging is disabled.
# ======================================================================================================================

import sys
import logging
logging.basicConfig(stream=sys.stdout)
logger = logging.getLogger()

from retry import retry
@retry(exceptions=(ValueError, TypeError), delay=3, tries=2, logger=logger )
def f2():
    raise ValueError


f2()


# WARNING:root:, retrying in 3 seconds...
#   File "C:/Oren/06 Computing/06 25 Python/bezpy_116_retry.py", line 31, in f2
#     raise ValueError
# ValueError