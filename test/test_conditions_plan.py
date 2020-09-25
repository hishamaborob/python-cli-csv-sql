from unittest import TestCase

from plan.conditions_plan import is_valid, is_record_included


class TestConditionsPlan(TestCase):
    def test_is_valid(self):
        is_conditions_plan_valid = is_valid(["city", "=", "Jerusalem", "and", "branch", "!=", "tech"])
        self.assertTrue(is_conditions_plan_valid)
        is_conditions_plan_valid = is_valid(["city", "=", "Jerusalem", "and", "branch"])
        self.assertFalse(is_conditions_plan_valid)

    def test_is_record_included(self):
        columns_positions = {"city": 0, "branch": 1}
        conditions = ["city", "=", "Jerusalem", "and", "branch", "=", "tech"]
        included_record = ["Jerusalem", "tech"]
        excluded_record = ["Petra", "travel"]
        is_included_record = is_record_included(included_record, conditions, columns_positions, 0)
        self.assertTrue(is_included_record)
        is_excluded_record = is_record_included(excluded_record, conditions, columns_positions, 0)
        self.assertFalse(is_excluded_record)
