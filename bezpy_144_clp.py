# ======================================================================================================================
# CLP Compressed Log Processor
# ======================================================================================================================
# Compressed Log Processor (CLP) is a tool capable of losslessly compressing text logs and searching the compressed logs without decompression.
# https://pypi.org/project/clp-logging/  Python log handler for the compressed logs
# python3 -m pip install --upgrade clp-logging
# ======================================================================================================================
# Ananth Korni presented 11/28/2023
# ======================================================================================================================
# •	Compressed Log Processor is a free tool capable of compressing text logs and searching the compressed logs without decompression
# •	CLP compression ratio is 2X of Gzip and the search is 4.2x faster than Splunk.
# •	replace all plain text logging to CLP custom format
# •	98% space savings compared to text logs
# •	A utility can be created to view/search the log files. It will leverage CLP python API


import logging
from pathlib import Path
from clp_logging.handlers import CLPFileHandler


# Text Log handler
text_logger = logging.getLogger(__name__)
text_logger.addHandler(logging.FileHandler('txt_logfile_1.log'))

# CLP Log Handler
clp_handler = CLPFileHandler(Path("example.clp.zst"))
logger = logging.getLogger(__name__)
logger.addHandler(clp_handler)
logger.warn("example warning")