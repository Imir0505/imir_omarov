
class BlockErrors:
    def __init__(self, err_types):
        self.err_types = err_types

    def __enter__(self):
        return self.err_types

    def __exit__(self, exc_type, exc_val, exc_tb):
        for i in self.err_types:
            if exc_type == i or issubclass(exc_type, i):
                return True

if __name__ == '__main__':
    err_types = {Exception}
    with BlockErrors(err_types):
        a = 1 / '0'
    print('Выполнено без ошибок')