"""GitHub API utilities.

Provides helper functions to fetch basic repository information.
"""

from typing import Dict
import logging

import requests


logger = logging.getLogger(__name__)


GITHUB_API_BASE = "https://api.github.com"


def get_repo_basic_info(owner: str, repo: str) -> Dict:
    """Fetch basic information for a GitHub repository.

    Args:
        owner: Repository owner (user or org).
        repo: Repository name.

    Returns:
        A dictionary containing selected repository metadata.

    Raises:
        requests.HTTPError: If the API request fails.
    """
    url = f"{GITHUB_API_BASE}/repos/{owner}/{repo}"
    logger.info("Fetching repo info from %s", url)

    response = requests.get(url, timeout=10)

    if response.status_code != 200:
        logger.error(
            "GitHub API request failed: %s %s",
            response.status_code,
            response.text,
        )
        response.raise_for_status()

    data = response.json()

    # Extract only commonly used fields
    return {
        "id": data.get("id"),
        "name": data.get("name"),
        "full_name": data.get("full_name"),
        "description": data.get("description"),
        "html_url": data.get("html_url"),
        "stargazers_count": data.get("stargazers_count"),
        "forks_count": data.get("forks_count"),
        "open_issues_count": data.get("open_issues_count"),
        "language": data.get("language"),
        "created_at": data.get("created_at"),
        "updated_at": data.get("updated_at"),
    }
