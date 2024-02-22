"""A module for getting the size of a pull request.

This module provides functions for getting the approximate pull request size 
as (additions + deletions) * 0.5.

Functions:
    get_pull_request_size(
        pull_request: github3.pulls.PullRequest
    ) -> int:
        Get approximate pull request size 
    get_stats_pull_request_size(
         issues_with_metrics: List[IssueWithMetrics]
    ) -> Union[int, None]:
        Calculate stats describing pull request size for a list of issues
        
"""

from typing import Union, List
from classes import IssueWithMetrics

import numpy
import github3

def get_stats_pull_request_size(
    issues_with_metrics: List[IssueWithMetrics]
) -> Union[int, None]:
    """
    Calculate stats describing the pull request size for a list of issues.
    """
    # Filter out issues with no size
    issues_with_pull_request_size = [
        issue for issue in issues_with_metrics if issue.pull_request_size is not None
    ]

    # Calculate the total size for all issues
    sizes = []
    if issues_with_pull_request_size:
        for issue in issues_with_pull_request_size:
            if issue.pull_request_size:
                sizes.append(issue.pull_request_size)

    # Calculate stats describing time to answer
    num_issues_with_pull_request_size = len(issues_with_pull_request_size)
    if num_issues_with_pull_request_size > 0:
        average_size = numpy.round(numpy.average(sizes))
        med_size = numpy.round(numpy.median(sizes))
        ninety_percentile_size = numpy.round(
            numpy.percentile(sizes, 90, axis=0)
        )
    else:
        return None

    stats = {
        "avg": average_size,
        "med": med_size,
        "90p": ninety_percentile_size,
    }

    # Print the average pull request size
    print(f"Average pull request size: {average_size}")
    return stats


def get_pull_request_size(
    pull_request: github3.pulls.PullRequest
) -> int:
    """
    Args:
        pull_request (github3.pulls.PullRequest): A GitHub pull request.

    Returns:
        int: The size of the pull request
    """

    additions = pull_request.additions_count
    deletions = pull_request.deletions_count

    size = (additions + deletions) * 0.5

    return size
