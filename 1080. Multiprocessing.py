import multiprocessing
import requests
import concurrent.futures


def downloadFile(url, name):
    print(f"Started Downloading {name}")

    response = requests.get(url)
    open(f"{name}.jpg", "wb").write(response.content)

    print(f"Finished Downloading {name}")


url = "https://picsum.photos/2000/3000"

pros = []

if __name__ == '__main__':
    for i in range(5):
        p = multiprocessing.Process(target=downloadFile, args=[url, i])

        p.start()
        pros.append(p)

    for p in pros:
        p.join()

# Started Downloading 0
# Started Downloading 2
# Started Downloading 4
# Started Downloading 1
# Started Downloading 3
# Finished Downloading 3
# Finished Downloading 2
# Finished Downloading 1
# Finished Downloading 0
# Finished Downloading 4


if __name__ == '__main__':
    with concurrent.futures.ProcessPoolExecutor() as executor:
        l1 = [url for i in range(5)]
        l2 = [i for i in range(5)]
        results = executor.map(downloadFile, l1, l2)
        for r in results:
            print(r)

# Started Downloading 0
# Started Downloading 1
# Started Downloading 2
# Started Downloading 3
# Started Downloading 4
# Finished Downloading 3
# Finished Downloading 4
# Finished Downloading 0
# None
# Finished Downloading 2
# Finished Downloading 1
# None
# None
# None
# None