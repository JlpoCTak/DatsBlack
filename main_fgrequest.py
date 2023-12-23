import fgrequests
import time

start = time.time()

sites = ['https://ya.ru']

def exception_handler(request, exception):
    print("Request failed")


response = fgrequests.build(sites, method='GET', worker=68)

for res in response:
    print(res)


end = time.time()
print(end - start, 'ms')
