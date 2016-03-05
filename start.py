from pages import pages_details
movie_box = "5e"
movie_box1 = []
movie_letter3 =["0","1","2","3","4","5","6","7","8"]
movie_letter4 =["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n"]
for i in movie_letter3:
  a = movie_box + i
  for j in movie_letter4:
    b = a + j
    movie_box1.append(b)
movie_box1.reverse()
movie = 'http://www.avmoo.net/cn/movie/'
movie_pages = []
for k in movie_box1:
    l = movie + k
    pages_details(l)
    print(k + '页打印完成')
print('抓取完成')