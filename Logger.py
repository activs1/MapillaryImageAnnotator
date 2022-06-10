from datetime import datetime


class Logger:
    """
    Date, time, fname, index
    """

    def __init__(self):
        self.file = 'log2'

    def log(self, fname, index, skip=False):
        now = str(datetime.now())
        with open(self.file, 'a') as file:
            file.write(f'{now} \t {fname} {"skipped" if skip else ""}')
            file.write('\n')
            file.write(f'{index}')
            file.write('\n')

    def get_last(self):
        file = open(self.file, 'r')
        try:
            last_line = file.readlines()[-1]
            if last_line == "":
                return 0
            return int(last_line)
        except:
            pass
        return 0
