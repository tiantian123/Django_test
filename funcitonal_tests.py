from selenium import webdriver
from selenium.webdriver.common.keys import Keys
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
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # 应用邀请输入一个代办事项
        inputbox = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(inputbox.get_attribute('placeholder'), 'Enter a to-do item')

        # 用户在一个文本框中输入了“buy peacock feathers(孔雀羽毛)”
        # 爱好是使用假蝇做鱼铒钓鱼
        inputbox.send_keys('Buy peacock feathers')

        # 用户回车后页面更新
        # 代办事项列表中显示了“1.Buy peacock feathers”
        inputbox.send_keys(Keys.ENTER)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_tag_name('tr')
        self.assertTrue(any(row.text == '1: Buy peacock feathers' for row in rows),
                        "New to-do item did not appear in table")

        # 页面又显示了一个文本框， 可以输入其他的代办事项
        # 用户输入了 “Use peacock feathers to make a fly(使用孔雀羽毛做假蝇)”
        # 用户做事很有条理
        self.fail("Finish the test")

        # 页面再次更新，用户的清单中显示了这2个待办事项

if __name__ == '__main__':
    unittest.main()