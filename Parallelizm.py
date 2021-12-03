from urllib.request import Request, urlopen
from urllib.parse import unquote
import time
import concurrent.futures

def load_url(url, timeout):
    request = Request(
        url,
        headers={'User-Agent': 'Mozilla/5.0 (Windows NT 9.0; Win65; x64; rv:97.0) Gecko/20105107 Firefox/92.0'},
    )
    resp = urlopen(request, timeout=timeout)
    resp.close()
    return resp.code

def main():
    links = open('res.txt', encoding='utf8').read().split('\n')

    start_time = time.time()
    with concurrent.futures.ThreadPoolExecutor(max_workers=100) as executor:
        future_to_url = {executor.submit(load_url, link, 5): link for link in links}
        for index, future in enumerate(concurrent.futures.as_completed(future_to_url), 1):
            url = future_to_url[future]
            try:
                response_code = future.result()
            except Exception as exc:
                print(f'{index} {url} generated an exception: {exc}')
            else:
                print(f'{index} {url} returns {response_code} code')

    print(f"Время выоплнения программы - {round(time.time() - start_time, 2)} сек")


if __name__ == '__main__':
    main()