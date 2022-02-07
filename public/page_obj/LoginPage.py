# 封装登录页面对象类，执行登录测试流程
import os,sys
from selenium import webdriver
from time import sleep
from config import setting
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from public.page_obj.base import Page
from public.models.GETYaml import getyaml

testData = getyaml(setting.TEST_Element_YAML +'/'+'login.yaml')

class login(Page):
    '''
    用户登录页面
    '''
    url = '/'
    dig_login_button_loc = (By.ID,testData.get_elementinfo(0))
    def dig_login(self):
        '''
        首页登录
        :return 
        '''
        self.find_element(*self.dig_login_button_loc.click())
        sleep(1)
    
    # 定位器，通过元素属性定位元素对象
    # 用户名的输入
    login_username_loc = (By.ID,testData.get_elementinfo(1))
    # 密码的输入框
    login_password_loc = (By.ID,testData.get_elementinfo(2))
    # 点击登录
    login_buttuon_loc = (By.ID,testData.get_elementinfo(3))

    def login_username(self,username):
        '''
        登录用户名
        :param username:
        :return :
        '''
        self.find_element(*self.login_username_loc).send_keys(username)

    def login_password(self,password):
        '''
        密码登录
        :param password:
        :return:
        '''
        self.find_element(*self.login_password_loc).send_keys(password)

    def login_button(self):
        '''
        登录按钮
        :return:
        '''
        self.find_element(*self.login_buttuon_loc).click()
    
    def user_login(self,username,password):
        '''
        登录入口
        :param username:用户名
        :param password:密码
        ：return： 
        '''
        self.open()
        self.dig_login()
        self.login_username(username)
        self.login_password(password)
        sleep(1)
        self.login_button()
        sleep(1)

    user_pawd_error_hint_loc = (By.XPATH,testData.get_CheckElementinfo(0))
    user_login_success_loc = (By.ID,testData.get_CheckElementinfo(1))
    pass_login_success_loc = (By.ID,testData.get_CheckElementinfo(2))

    # 用户名或密码输入错误的提示
    def user_pawd_error_hint(self):
        return self.find_element(*self.user_pawd_error_hint_loc).text
    
    # 用户名登录成功
    def user_login_success_hint(self):
        return self.find_element(*self.user_login_success_loc).text()
    
    # 密码登录成功
    def pass_login_success_hint(self):
        return self.find_element(*self.pass_login_success_loc).text



