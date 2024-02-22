"""This module provides unit tests for the time_to_answer module."""

import unittest
from typing import List

from classes import IssueWithMetrics
from pull_request_size import get_stats_pull_request_size, get_pull_request_size


class TestGetAveragePullRequestSize(unittest.TestCase):
    """A test case for the get_stats_pull_request_size function.

    This test case includes three test methods:
    - test_returns_none_for_empty_list
    - test_returns_none_for_list_with_no_pull_request_size
    - test_returns_stats_pull_request_size
    """

    def test_returns_none_for_empty_list(self):
        """Tests that the function returns None when given an empty list of issues."""
        # Arrange
        issues_with_metrics: List[IssueWithMetrics] = []

        # Act
        result = get_stats_pull_request_size(issues_with_metrics)

        # Assert
        self.assertIsNone(result)

    def test_returns_none_for_list_with_no_pull_request_size(self):
        """
        Tests that the function returns None when given a list of
        issues with no pull request size.
        """
        # Arrange
        issues_with_metrics = [
            IssueWithMetrics("issue1", None, None),
            IssueWithMetrics("issue2", None, None),
        ]

        # Act
        result = get_stats_pull_request_size(issues_with_metrics)

        # Assert
        self.assertIsNone(result)

    def test_returns_stats_pull_request_size(self):
        """
        Tests that the function correctly calculates the average
        pull request size for a list of issues with pull request size.
        """

        # Arrange
        issues_with_metrics = [
            IssueWithMetrics("issue1", "url1", "alice", None, None, None, None, 250),
            IssueWithMetrics("issue2", "url2", "bob", None, None, None, None, 250),
            IssueWithMetrics("issue3", "url3", "carol", None, None, None, None, 550),
        ]

        # Act
        result = get_stats_pull_request_size(issues_with_metrics)

        # Assert
        self.assertEqual(result["avg"], 350);
        self.assertEqual(result["med"], 250);
