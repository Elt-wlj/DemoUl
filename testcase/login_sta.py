import os,sys
sys.path.append(os.path.dirname(os.path.dirname(__file__)))
import unittest,ddt,yaml
from config import setting
from public.models import myunit,screenshot
from public.page_obj.LoginPage import login
from public.models.log import Log
try:
    f = open(setting.TEST_DATA_YAML  + '/' + 'login_data.yaml',encoding='utf-8')
    testData = yaml.load(f)
except FileNotFoundError as file:
    log = Log()
    log.error('文件不存在：{0}'.format(file))

@ddt.ddt
class Demo_UI(myunit.MyTest):
    '''
    服务中心系统登录测试
    '''
    def user_login_verify(self,username,password):
        '''
        用户登录
        :param username:用户名
        :param password:密码
        :return :
        '''
        login (self.driver).user_login(username,password)
    
    @ddt.data(*testData)
    def test_login(self,datayaml):
        '''
        登录测试
        ：param datayaml:接在login_data登录测试数据
        :return :
        '''
        log = Log()
        log.info('当前执行测试用例ID ->{0};测试点 - >{1}'.format(datayaml['detail']))
        # 调用登录方法
        self.user_login_verify(datayaml['data']['username'],datayaml['data']['password'])
        po = login(self.driver)
        
        if datayaml['screenshot'] == 'user_pawd_success':
            log.info('检查点 ->{0}'.format(po.user_login_success_hint()))
            self.assertEqual(po.user_login_success_hint(),datayaml['check'][0],'成功登录，返回实际结果是 ->:{0}'.format(po.user_login_success_hint))
            screenshot.insert_img(self.driver,datayaml['screenshot']+'jpg')
        else:
            log.info('检查点->{0}'.format(po.user_pawd_error_hint()))
            self.assertEqual(po.user_pawd_error_hint(),datayaml['check'][0],'登录错误，返回实际结果是->:{0}'.format(po.user_pawd_error_hint()))
            log.info('登录错误，返回实际结果->{0}'.format(po.user_pawd_error_hint()))
            screenshot.insert_img(self.driver,datayaml['screenshot'+'.jpg'])
    
if __name__=='__main__':
    unittest.main()


