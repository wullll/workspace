#!/usr/bin/python
# coding=utf-8

import uiautomator2
from time import sleep
import unittest

# uiautomator2.UIAutomatorServer
"""
{'text': (1, None), 'textContains': (2, None), 'textMatches': (4, None), 'textStartsWith': (8, None), 
'className': (16, None), 'classNameMatches': (32, None), 'description': (64, None), 'descriptionContains': (128, None),
 'descriptionMatches': (256, None), 'descriptionStartsWith': (512, None), 'checkable': (1024, False), 
 'checked': (2048, False), 'clickable': (4096, False), 'longClickable': (8192, False), 'scrollable': (16384, False),
  'enabled': (32768, False), 'focusable': (65536, False), 'focused': (131072, False), 'selected': (262144, False),
   'packageName': (524288, None), 'packageNameMatches': (1048576, None), 'resourceId': (2097152, None),
    'resourceIdMatches': (4194304, None), 'index': (8388608, 0), 'instance': (16777216, 0)}
"""


class UiAutoTest(unittest.TestCase):

    def test_add(self):
        d = uiautomator2.connect()
        d.app_stop_all()
        # print(d.device_info)
        # package name :com.youdao.calculator
        # d.adb_shell('am force-stop com.youdao.calculator')
        # print(d.wait_timeout, d.window_size(), d.platform)
        sleep(3)
        # 启动app
        sess = d.session("com.youdao.calculator")
        sleep(3)
        # 输入1  d(resourceId="com.youdao.calculator:id/iv_icon", className="android.widget.ImageView", instance=16)
        d(resourceId="com.youdao.calculator:id/iv_icon", className="android.widget.ImageView", instance=16).click()
        # 输入+  d(resourceId="com.youdao.calculator:id/iv_icon", className="android.widget.ImageView", instance=19)
        d(resourceId="com.youdao.calculator:id/iv_icon", className="android.widget.ImageView", instance=19).click()
        # 1
        d(resourceId="com.youdao.calculator:id/iv_icon", className="android.widget.ImageView", instance=16).click()
        # =
        d(className="android.widget.FrameLayout", instance=55).click()
        # sleep(5)
        d(description=u"=", className="android.view.View").click()
        # d(description="=").click()
        sess.screenshot("screen.png")
        sleep(3)
        d.app_stop("com.youdao.calculator")


if __name__ == "__main__":
    unittest.main()