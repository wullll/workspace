#!/usr/lib/python
# -*-coding:utf-8-*-
import time
from unittest import TestCase, main
from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction


class AppiumTest(TestCase):

    # 加载驱动
    def setUp(self):
        print("setUp method")
        desired_caps = {'platformName': 'Android',  # 声明是ios还是Android系统
                        'platformVersion': '5.1',   # Android内核版本号,可以在夜神模拟器设置中查看
                        'deviceName': '127.0.0.1:62025 device',  # 连接的设备名称
                        # 'app': 'D:\\android\Emmagee2.4.apk',
                        'appPackage': 'com.youdao.calculator',   # apk的包名
                        'appActivity': 'com.youdao.calculator.activities.MainActivity',  # apk的launcherActivity
                        'noReset': True,
                        'unicodeKeyboard': 'True'}
        self.wd = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
        self.wd.implicitly_wait(60)

    def tearDown(self):
        print("tearDown method")
        self.wd.close_app()

    def test_one(self):
        print("test method")
        time.sleep(3)
        wd = self.wd
        print(wd)
        wd.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.FrameLayout\").index(16)").click()
        wd.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.FrameLayout\").index(19)").click()
        wd.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.FrameLayout\").index(17)").click()
        wd.find_element_by_android_uiautomator(
            "new UiSelector().className(\"android.widget.FrameLayout\").index(24)").click()
        action = TouchAction(wd)
        wd.get_window_size()
        action.tap(None, 75, 225)
        # wd.tap((75, 225))
        wd.save_screenshot("name.png")
        time.sleep(5)


if __name__ == "__main__":
    main()
