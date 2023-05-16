import multiprocessing
import requests
from concurrent.futures import ProcessPoolExecutor


def downloadFile(url, name):
    print(f"Started Download {name}")
    response = requests.get(url)
    open(f"photos/{name}.jpg", "wb").write(response.content)
    print(f"Finished Download {name}")


url = "https://picsum.photos/2000/3000"

# pros = []
# for i in range(50):
#     # downloadFile(url, i)
#     p = multiprocessing.Process(target=downloadFile, args=[url, i])
#     p.start()
#     pros.append(p)
#
#
# for p in pros:
#     p.join()


with ProcessPoolExecutor() as executor:
    l1 = [url for i in range(60)]
    l2 = [i for i in range(60)]
    results = executor.map(downloadFile, l1, l2)
    for r in results:
        print(r)
