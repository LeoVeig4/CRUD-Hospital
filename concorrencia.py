# -*- coding: utf-8 -*-
from concurrent.futures import ThreadPoolExecutor, as_completed
import requests

def get(url, timeout):
    return requests.get('http://127.0.0.1:5000', timeout=5000)

def requestUrls(urls, timeout=5):
    with ThreadPoolExecutor(max_workers=50) as executor:
        agenda = {executor.submit(get, url, timeout): url for url in urls}

        for tarefa in as_completed(agenda):
            try:
                conteudo = tarefa.result()
            except Exception as e:
                print("Não foi possível fazer a requisição!\n{}".format(e))
            else:
                yield conteudo

urls = ['https://www.python.org/', 'https://pypi.python.org/pypi/requests', 'http://pt.stackoverflow.com/']
requisicoes = requestUrls(urls)

for requisicao in requisicoes:
    codigo = requisicao.status_code
    url = requisicao.url
    conteudo = requisicao.content

    print("{}: {}".format(codigo, url))
