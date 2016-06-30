#coding=utf-8
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.common.exceptions import NoSuchElementException
import unittest, time, re
import HTMLTestRunner


class My_Test_Suite(unittest.TestCase):
  u'''打印百度、google标题'''
  def setUp(self):
    self.driver = webdriver.Ie()
    self.driver.implicitly_wait(30)
    self.verificationErrors = []
    self.accept_next_alert = True

  def test_baidu(self):
    u'''打开百度'''
    driver = self.driver
    driver.get("http://www.baidu.com")
    print u'当前网页是:',driver.title
    driver.close()

  def test_google(self):
    u'''打开google'''
    driver = self.driver
    driver.get("http://www.renren.com")
    print u'当前网页是:',driver.title

  def tearDown(self):
    self.driver.quit()
    self.assertEqual([], self.verificationErrors)

if __name__ == "__main__":

  #定义一个单元测试容器
  testunit=unittest.TestSuite()

  #将测试用例加入到测试容器中
  testunit.addTest(My_Test_Suite("test_baidu"))
  testunit.addTest(My_Test_Suite("test_google"))

  #定义个报告存放路径，支持相对路径
  filename = 'C:\\Users\\kerwin\\Desktop\\HTMLTestRunner-master\\HTMLTestRunner-master\\result.html'

  fp = file(filename, 'wb')
  #定义测试报告
  runner =HTMLTestRunner.HTMLTestRunner(stream=fp,title=u'测试报告',description=u'用例执行详情:：')

  #运行测试用例
  runner.run(testunit)
