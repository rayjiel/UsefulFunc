简单多线程
内容来源：https://www.gairuo.com/p/python-requests
由于 Selenium 太慢，可以用多线程解决。以下是一个简单的多线程用户示例：

# 爬虫
def get_data(page_id):
    url = f'https://xxxPage?Id='
    r = s.get(url)
    df = pd.DataFrame(r.json()['data']['items'])
    df.to_csv(f'card/xxx-{page_id}.csv')
    print(f'{page_id}页已获取')

# 定义好爬虫及传值范围
def run(start, end):
    for i in range(start, end+1):
        get_data(i)

# 引入相关库
import threading
import time

# 分批同时执行
%%time
t1 = threading.Thread(target=run, args=(1, 100))
t2 = threading.Thread(target=run, args=(101, 200))
t3 = threading.Thread(target=run, args=(201, 300))

t1.start()
t2.start()
t3.start()
