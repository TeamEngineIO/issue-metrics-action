"""This module provides unit tests for the time_to_answer module."""

import unittest
from unittest.mock import MagicMock
from typing import List

from classes import IssueWithMetrics
from pull_request_size import get_stats_pull_request_size, get_pull_request_size


class TestGetAveragePullRequestSize(unittest.TestCase):
    """A test case for the get_stats_pull_request_size and get_pull_request_size functions.

    This test case includes three test methods for get_stats_pull_request_size:
    - test_returns_none_for_empty_list
    - test_returns_none_for_list_with_no_pull_request_size
    - test_returns_stats_pull_request_size

    And three test methods for get_pull_request_size:
    - test_get_pull_request_size
    - test_get_pull_request_size_no_additions
    - test_get_pull_request_size_no_deletions
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

    def test_get_pull_request_size(self):
        """Test that the function correctly gets the pull request size"""
        pull_request = MagicMock()
        pull_request.additions_count = 100;
        pull_request.deletions_count = 100;

        result = get_pull_request_size(pull_request)
        expected_result = 100;
        self.assertEqual(result, expected_result)
    
    def test_get_pull_request_size_no_additions(self):
        """Test that the function correctly gets the pull request size when there are only deletions"""
        pull_request = MagicMock()
        pull_request.additions_count = 0;
        pull_request.deletions_count = 300;

        result = get_pull_request_size(pull_request)
        expected_result = 300;
        self.assertEqual(result, expected_result)
    
    def test_get_pull_request_size_no_deletions(self):
        """Test that the function correctly gets the pull request size when there are only additions"""
        pull_request = MagicMock()
        pull_request.additions_count = 200;
        pull_request.deletions_count = 0;

        result = get_pull_request_size(pull_request)
        expected_result = 200;
        self.assertEqual(result, expected_result)
