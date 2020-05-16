from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self) -> None:
        self.browser = webdriver.Firefox()
        self.browser.implicitly_wait(3)

    def tearDown(self) -> None:
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_later(self):
        # 听说有一个很酷的在线代办事项应用
        # 现在去看一下这个应用的首页
        self.browser.get('http://localhost:8000')

        # 可以注意到网页的标题和头部都包含“To-Do” 这个词
        self.assertIn('To-Do', self.browser.title)
        self.fail('finish the test')

        # 应用邀请输入一个代办事项

if __name__ == '__main__':
    unittest.main()