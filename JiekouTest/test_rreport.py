import HTMLTestRunner

# HTMLTestRunner.main()
import unittest

from test_login import TestLogin

fp = open('my_report.html', 'wb')
suite = unittest.TestLoader().loadTestsFromTestCase(TestLogin)
runner = HTMLTestRunner.HTMLTestRunner(
    stream=fp,
    title='My unit test',
    description='This demonstrates the report output by HTMLTestRunner.'
)
runner.run(suite)
unittest.main(verbosity=2)
fp.close()
