import requests


class Connection:
    def get_json(self, url):
        raise NotImplementedError


class Request(Connection):
    def __init__(self):
        self.fetch = requests

    def get_json(self, url):
        response = self.fetch.get(url)
        return response.json()


class NewRequest(Connection):
    def __init__(self, fetch):
        self.fetch = fetch

    def get_json(self, url):
        pass


# https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11
class ApiClient:
    def __init__(self, fetch: Connection):
        self.fetch = fetch

    def get_json(self, url):
        response = self.fetch.get_json(url)
        return response


def pretty_view(data: list[dict]):
    pattern = '|{:^10}|{:^10}|{:^10}|'
    print(pattern.format('currency', 'sale', 'buy'))
    for el in data:
        currency, *_ = el.keys()
        buy = el.get(currency).get('buy')
        sale = el.get(currency).get('sale')
        print(pattern.format(currency, sale, buy))


def data_adapter(data: dict) -> list[dict]:
    return [{f"{el.get('ccy')}": {"buy": float(el.get('buy')), "sale": float(el.get('sale'))}} for el in data]


if __name__ == "__main__":
    client = ApiClient(Request())
    data = client.get_json(
        "https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11"
    )
    pretty_view(data_adapter(data))

    # con = Connection()
    # con.get_json("https://api.privatbank.ua/p24api/pubinfo?exchange&coursid=11")
    