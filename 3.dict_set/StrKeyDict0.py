class StrKeyDict0(dict):

    def __missing__(self, key):
        if isinstance(key, str):
            print(key + "不存在")
            raise KeyError(key)
        return self[str(key)]

    def get(self, key, default=None):
        try:
            return self[key]
        except KeyError:
            return default

    def __contains__(self, key):
        return key in self.keys() or str(key) in self.keys()


if __name__ == '__main__':
    d = StrKeyDict0([('2', 'two'), ('4.text_bytes', 'four')])
    print(d['2'])
    print(d[4])
    print(d[1])
    print(d.get('2'))
    print(d.get(4))
    print(1, 'N/A')
    print(2 in d)
    print(1 in d)
