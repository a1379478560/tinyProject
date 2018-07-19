from zhihu_oauth import ZhihuClient

client = ZhihuClient()

client.load_token('token.pkl')

me = client.me()

print('name', me.name)
print('headline', me.headline)
print('description', me.description)

print('following topic count', me.following_topic_count)
print('following people count', me.following_count)
print('followers count', me.follower_count)

print('voteup count', me.voteup_count)
print('get thanks count', me.thanked_count)

print('answered question', me.answer_count)
print('question asked', me.question_count)
print('collection count', me.collection_count)
print('article count', me.articles_count)
print('following column count', me.following_column_count)



# from zhihu_oauth import ZhihuClient
# from zhihu_oauth.exception import NeedCaptchaException
# client = ZhihuClient()
# user = '619400536@qq.com'
# pwd = 'a130129'
# try:
#     client.login(user, pwd)
#     print(u"登陆成功!")
# except NeedCaptchaException: # 处理要验证码的情况
#     # 保存验证码并提示输入，重新登录
#     with open('a.gif', 'wb') as f:
#         f.write(client.get_captcha())
#     captcha = input('please input captcha:')
#     client.login(user, pwd, captcha)
#
# client.save_token('token.pkl') # 保存token
# #有了token之后，下次登录就可以直接加载token文件了
# # client.load_token('filename')