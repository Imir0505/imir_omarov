import sys

class Redirect:
    def __init__(self, stdout=None, stderr=None):
        self.stdout_new = stdout
        self.stderr_new = stderr
        self.stdout_old = None
        self.stderr_old = None

    def __enter__(self):
        if self.stdout_new is not None:
            self.stdout_old = sys.stdout
            sys.stdout = self.stdout_new
        if self.stderr_new is not None:
            self.stderr_old = sys.stderr
            sys.stderr = self.stderr_new


    def __exit__(self, exc_type, exc_val, exc_tb):
        if self.stdout_new is not None:
            sys.stdout = self.stdout_old
        if self.stderr_new is not None:
            sys.stderr = self.stderr_old


if __name__ == '__main__':
    print('Hello stdout')
    stdout_file = open('stdout.txt', 'w')
    stderr_file = open('stderr.txt', 'w')

    with Redirect(stdout=stdout_file, stderr=stderr_file):
        print('Hello stdout.txt')
        raise Exception('Hello stderr.txt')


    print('Hello stdout again')
    raise Exception('Hello stderr')