class Result:
    def __init__(self, header=None, records=None, count=None):
        self.__header = header
        self.__records = records
        if count:
            self.__count = count
        elif bool(self.__records):
            self.__count = len(records)
        else:
            self.__count = 0

    def get_header(self) -> tuple:
        return self.__header

    def get_records(self) -> tuple:
        return self.__records

    def get_count(self):
        return self.__count

    def print(self):
        return str(self.__header)+str(self.__records)+str(self.__count)


def empty_result():
    return Result(count=0)
