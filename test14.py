#发短信
# from twilio.rest import Client
#
# # Your Account SID from twilio.com/console
# account_sid = "AC2629ab29bb514888ec3cf66a4d287399"
# # Your Auth Token from twilio.com/console
# auth_token  = "0186102ffd934f4c48b2e4f60d5cc4e0"
#
# client = Client(account_sid, auth_token)
#
# message = client.messages.create(
#     to="+8615262691505",
#     from_="+18474166549",
#     body="Hello from Python!")
#
# print(message.sid)

#冒犯用语检测
# import urllib.request
# def read_txt():
#     f = open("movie_quotes.txt")
#     content = f.read()
#     #print(content)
#     f.close()
#     check(content)
# def check(txt):
#     f = urllib.request.urlopen("http://www.wdylike.appspot.com/?q="+txt)#打开网站，检测文字
#     print(f.read())
#     f.close()
#
# read_txt()

#电影网页
import media
import fresh_tomato
movie1 = media.Movie("记忆大师",
                    "关于记忆的悬疑故事",
                    "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=记忆大师海报&hs=2&pn=0&spn=0&di=13146585650&pi=0&rn=1&tn=baiduimagedetail&is=0%2C0&ie",
                    "https://v.youku.com/v_show/id_XMjczMDM1ODA0NA")
#print(movie1.title)
#movie1.show_trailer()
#movie1.show_poster()
movie2 = media.Movie("摔跤吧！爸爸",
                     "关于一个摔跤手的励志故事",
                     "https://image.baidu.com/search/detail?ct=503316480&z=0&ipn=d&word=摔跤吧爸爸海报&hs=2&pn=1&spn=0&di=94079068821&pi=0&rn=1&tn=baiduimagedetail&is",
                     "https://v.youku.com/v_show/id_XMjcyNDg0ODE1Mg")

movies = [movie1, movie2]
#fresh_tomato.open_movies_page(movies)
print(movie1.VALID_RATING) #VALID_RATING是类变量，通常全部大写，表示不常改变
print(movie1.__doc__)  # __doc__是类中预定义的类变量（不需要认为定义的），内容关于类的说明文档


