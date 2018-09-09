import time

from selenium import webdriver as wd
from selenium.webdriver.common.keys import Keys


class Insta(object):

    def __init__(self, username, password):
        self.username = username
        self.password = password
        self.driver = wd.Chrome()

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")

        self.driver.find_element_by_xpath("//div/input[@name='username']").send_keys(self.username)
        self.driver.find_element_by_xpath("//div/input[@name='password']").send_keys(self.password)
        self.driver.find_element_by_xpath("//span/button").click()

    def scrape_followers(self):
        # Load account page
        time.sleep(2)
        self.driver.get("https://www.instagram.com/{0}/".format(self.username))

        # Click the 'Follower(s)' link
        self.driver.find_element_by_partial_link_text("seguidores").click()
        time.sleep(2)

        # xpath = "/html/body/div[4]/div/div/div[2]/div/div[2]/ul/li"

        dialog = self.driver.find_element_by_xpath('/html/body/div[3]/div/div/div[2]')
        time.sleep(1)
        actions = wd.ActionChains(self.driver)
        time.sleep(1)
        actions.move_to_element(dialog)
        time.sleep(1)

        actions.click()
        time.sleep(1)
        actions.send_keys(Keys.SPACE)  # Replace with whichever keys you want.
        actions.perform()
        time.sleep(1)
        actions.send_keys(Keys.SPACE)  # Replace with whichever keys you want.
        actions.perform()
        time.sleep(1)
        actions.send_keys(Keys.SPACE)  # Replace with whichever keys you want.
        actions.perform()
        time.sleep(10)

        # dialog.click()
        # print "HEREaaassssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssssa"
        # time.sleep(2)
        # dialog.click()
        # dialog.send_keys(Keys.SPACE)
        # time.sleep(10)
        # scroll_xpath = '/html/body/div[2]/div/div/div[2]'
        # element = driver.find_elements_by_xpath(scroll_xpath)

        # NOT WORKING driver.execute_script("return arguments[0].scrollIntoView();", element)
        # driver.execute_script("return arguments[0].scrollIntoView(true);", element)

        # driver.execute_script("arguments[0].scrollTop = arguments[0].scrollHeight", element)

        # xpath = "/html/body/div[3]/div/div/div[2]/ul"
        #
        # followers_elems = driver.find_elements_by_xpath(xpath)
        #
        # followers_temp = [e.text for e in followers_elems]  # List of followers (username, full name, follow text)
        # followers = []  # List of followers (usernames only)
        #
        # # Go through each entry in the list, append the username to the followers list
        # for i in followers_temp:
        #     username, sep, name = i.partition('\n')
        #     followers.append(username)
        #
        # print("______________________________________")
        # print("FOLLOWERS")
        #
        # return followers


