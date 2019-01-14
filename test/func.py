import top.api

appkey="25233423"
secret="65c19f4b8b95c7ea9ece09adf10ac208"

req=top.api.TbkDgItemCouponGetRequest()
req.set_app_info(top.appinfo(appkey,secret))

req.adzone_id=1
req.platform=1
req.cat=""
req.page_size=1
req.q="女装"
req.page_no=1
try:
	resp= req.getResponse()
	print(resp)
except :
	raise