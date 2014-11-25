import unittest

import prettycron


class PrettyCronTest(unittest.TestCase):
    def test_yearly(self):
        self.assertEqual(prettycron.prettify("0 0 1 1 *"), "At 00:00 on the 1st of January")

    def test_one_day_in_month(self):
        self.assertEqual(prettycron.prettify("0 0 1 * *"), "At 00:00 on the 1st of every month")

    def test_every_day_in_month(self):
        self.assertEqual(prettycron.prettify("12 15 * 1 *"), "At 15:12 every day in January")

    def test_every_specific_day_in_month(self):
        self.assertEqual(prettycron.prettify("0 0 * 1 1"), "At 00:00 on every Monday in January")

    def test_weekly(self):
        self.assertEqual(prettycron.prettify("0 0 * * 0"), "At 00:00 on every Sunday")

    def test_monthly_and_weekly(self):
        self.assertEqual(prettycron.prettify("0 0 1 * 1"), "At 00:00 on the 1st of every month and on every Monday")

    def test_every_specific_day_in_month_and_weekly(self):
        self.assertEqual(prettycron.prettify("0 0 1 1 1"), "At 00:00 on the 1st of January and on every Monday in January")

    def test_daily(self):
        self.assertEqual(prettycron.prettify("0 0 * * *"), "At 00:00 every day")

    def test_hourly(self):
        self.assertEqual(prettycron.prettify("0 * * * *"), "At 0 minutes past every hour of every day")

    def test_minutely(self):
        self.assertEqual(prettycron.prettify("* 5 * * *"), "Every minute between 05:00 and 05:59 every day")

    def test_continuous(self):
        self.assertEqual(prettycron.prettify("* * * * *"), "Every minute of every day")

    def test_unsupported(self):
        self.assertEqual(prettycron.prettify("* */6 * * *"), "* */6 * * *")
