class Average:

    def __init__(self):
        self.series = []

    def __call__(self, new_vale):
        self.series.append(new_vale)
        total = sum(self.series)
        return total/len(self.series)


if __name__ == '__main__':
    avg = Average()
    print(avg(10))
    print(avg(11))
    print(avg(12))
