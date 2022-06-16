from typing import List
from time import sleep
from selenium import webdriver as wd
from selenium.common.exceptions import ElementClickInterceptedException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from utils.exceptions import ArgumentError, ElementNotFoundError


class WebdriverOption:
    """初始化测试驱动，封装常用操作"""

    def __init__(self, driver: wd.Chrome) -> None:
        self.driver = driver
        self.action = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 30)

    def open_website(self, url):
        """打开网址"""
        return self.driver.get(url)

    def find_elements(self, locator) -> List[WebElement]:
        """定位元素，支持XPATH和CSS SELECTOR定位，若找到则返回一个元素对象列表，没找到返回空列表"""
        if '//' in locator:
            ele = self.driver.find_elements(By.XPATH, locator)
        elif '.' in locator or '#' in locator or '>' in locator:
            ele = self.driver.find_elements(By.CSS_SELECTOR, locator)
        else:
            raise ArgumentError
        if len(ele):
            return ele
        raise ElementNotFoundError(locator)

    def get_element_num(self, locator):
        """获取元素的个数"""
        return len(self.find_elements(locator))

    def wait_element_visibility(self, locator, timeout=30):
        """等待元素出现，DOM上已存在且display为true"""
        try:
            if '//' in locator or '/' in locator:
                WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.XPATH, locator)))
            elif '.' in locator or '#' in locator or '>' in locator:
                WebDriverWait(self.driver, timeout).until(EC.visibility_of_element_located((By.CSS_SELECTOR, locator)))
            else:
                raise ArgumentError
            return True
        except ArgumentError:
            raise
        except Exception:
            return False

    def wait_element_invisibility(self, locator, timeout=30):
        """等待元素不可见，DOM上不存在了或者display为None"""
        try:
            if '//' in locator or '/' in locator:
                WebDriverWait(self.driver, timeout).until(EC.invisibility_of_element_located((By.XPATH, locator)))
            elif '.' in locator or '#' in locator or '>' in locator:
                WebDriverWait(self.driver, timeout).until(
                    EC.invisibility_of_element_located((By.CSS_SELECTOR, locator)))
            else:
                raise ArgumentError
            return True
        except ArgumentError:
            raise
        except Exception:
            return False

    def wait_element_clickable(self, locator, timeout=30):
        """等待元素直到其可被点击"""
        try:
            if '//' in locator or '/' in locator:
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.XPATH, locator)))
            elif '.' in locator or '#' in locator or '>' in locator:
                WebDriverWait(self.driver, timeout).until(EC.element_to_be_clickable((By.CSS_SELECTOR, locator)))
            else:
                raise ArgumentError
            return True
        except ArgumentError:
            raise
        except Exception:
            return False

    def screenshot(self, save_path):
        self.driver.save_screenshot(save_path)

    def moveto(self, locator):
        """鼠标移动到某个元素的中间位置"""
        if isinstance(locator, WebElement):
            return self.action.move_to_element(locator).perform()
        return self.action.move_to_element(self.find_elements(locator)[0]).perform()

    def click(self, locator, order=1, focus=False, text=None):
        """点击元素"""
        if text:
            if isinstance(locator[0], WebElement):
                for el in locator:
                    if self.get_text(el) == text:
                        el.click()
                        break
            else:
                for el in self.find_elements(locator):
                    if self.get_text(el) == text:
                        el.click()
                        break
        else:
            if isinstance(locator, WebElement):
                if focus:
                    self.driver.execute_script("arguments[0].scrollIntoView();", locator)
                    sleep(1)
                return locator.click()
            ele = self.find_elements(locator)
            if abs(order) > len(ele):
                raise IndexError
            elif order == 0:
                raise IndexError
            elif order < 0:
                el = ele[order]
                try:
                    if focus:
                        self.driver.execute_script("arguments[0].scrollIntoView();", el)
                        sleep(1)
                    el.click()
                except ElementClickInterceptedException:
                    sleep(2)
                    el.click()
                except Exception:
                    raise
            else:
                el = ele[order - 1]
                try:
                    if focus:
                        self.driver.execute_script("arguments[0].scrollIntoView();", el)
                        sleep(1)
                    el.click()
                except ElementClickInterceptedException:
                    sleep(2)
                    el.click()
                except Exception:
                    raise

    def double_click(self, locator):
        """双击元素"""
        el = self.find_elements(locator)[0]
        ActionChains(self.driver).double_click(el).perform()

    def input_text(self, locator, text=None, order=0):
        """输入内容，返回输入框元素类型"""
        ele = self.find_elements(locator)[order]
        ele.send_keys(text)
        return ele

    def input_text_enter(self, locator, text=None):
        """输入内容，点击回车"""
        self.find_elements(locator)[0].send_keys(text, Keys.ENTER)
        sleep(1)

    def refresh(self):
        """刷新页面"""
        return self.driver.refresh()

    def maximize_window(self):
        return self.driver.maximize_window()

    def minimize_window(self):
        return self.driver.minimize_window()

    def back(self):
        self.driver.back()

    def forward(self):
        self.driver.forward()

    def switch_to_url(self, url):
        self.find_elements('//body')[0].send_keys(Keys.CONTROL, 't')
        sleep(1)
        self.open_website(url)

    def switch_to_new_tab(self, url):
        self.driver.execute_script(f"window.open('{url}','_blank');")
        sleep(1)
        self.driver.switch_to.window(self.driver.window_handles[-1])

    def get_text(self, element):
        """
        des：获取标签中的文字内容
        element：元素
        """
        if isinstance(element, WebElement):
            return element.text
        else:
            ele = self.find_elements(element)[0]
            if ele and isinstance(ele, WebElement):
                return ele.text
            return

    def get_class(self, element: WebElement):
        """
        des：获取标签中的文字内容
        element：元素
        """
        return element.get_attribute('class')
