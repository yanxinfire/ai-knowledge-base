"""Collector agent.

Responsible for fetching and filtering raw data from external sources.
"""

from typing import List, Dict
import logging


logger = logging.getLogger(__name__)


def collect_sources(limit: int) -> List[Dict]:
    """Collect raw data from external sources.

    Args:
        limit: Number of items to collect.

    Returns:
        A list of raw data dictionaries.
    """
    logger.info("Collecting data from sources with limit=%s", limit)
    return []
