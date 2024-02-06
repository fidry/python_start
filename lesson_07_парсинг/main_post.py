import json

import requests
from fake_useragent import FakeUserAgent


headers = {
    'authority': 'interface.gateway.uniswap.org',
    'accept': '*/*',
    'accept-language': 'ru-RU,ru;q=0.9,en-US;q=0.8,en;q=0.7',
    'content-type': 'text/plain;charset=UTF-8',
    'origin': 'https://app.uniswap.org',
    'referer': 'https://app.uniswap.org/',
    'sec-ch-ua': '"Not A(Brand";v="99", "Google Chrome";v="121", "Chromium";v="121"',
    'sec-ch-ua-mobile': '?0',
    'sec-ch-ua-platform': '"macOS"',
    'sec-fetch-dest': 'empty',
    'sec-fetch-mode': 'cors',
    'sec-fetch-site': 'same-site',
    'user-agent': FakeUserAgent().random,
    'x-request-source': 'uniswap-web',
}

data = {
    "tokenInChainId": 42161,
    "tokenIn": "ETH",
    "tokenOutChainId": 42161,
    "tokenOut": "0xFd086bC7CD5C481DCC9C85ebE478A1C0b69FCbb9",
    "amount": "1000000000000000",
    "sendPortionEnabled": True,
    "type": "EXACT_INPUT",
    "intent": "quote",
    "configs": [
        {
            "protocols": ["V2", "V3", "MIXED"],
            "enableUniversalRouter": True,
            "routingType": "CLASSIC",
            "recipient": "0x36F302d18DcedE1AB1174f47726E62212d1CcEAD",
            "enableFeeOnTransferFeeFetching": True
        }
    ]
}

response = requests.post('https://interface.gateway.uniswap.org/v2/quote', headers=headers, data=json.dumps(data))
print(response.status_code)
print(response.json())
print(
    int(response.json()['quote']['quote']) / 10 ** 6
)
