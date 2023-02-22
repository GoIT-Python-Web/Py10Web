from storage import Storage, JSONStorage, YAMLStorage


class Service:
    def __init__(self, storage: Storage):
        self.storage = storage

    def get(self, key):
        return self.storage.get_value(key)


if __name__ == '__main__':
    sj = Service(JSONStorage('data.json'))
    print(sj.get("name"), sj.get("age"))

    sy = Service(YAMLStorage('data.yaml'))
    print(sy.get("name"), sy.get("age"))
