'''
Created by auto_sdk on 2018.07.25
'''
from top.api.base import RestApi
class TbkUatmEventGetRequest(RestApi):
	def __init__(self,domain='gw.api.taobao.com',port=80):
		RestApi.__init__(self,domain, port)
		self.fields = None
		self.page_no = None
		self.page_size = None

	def getapiname(self):
		return 'taobao.tbk.uatm.event.get'
