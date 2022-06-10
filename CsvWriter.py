
PATH = 'data.csv'


class CsvWriter:

    @staticmethod
    def append_row(fname, _class):
        if _class == 'highway':
            line = f'{fname}, 1, 0, 0'
        elif _class == 'countryside':
            line = f'{fname}, 0, 1, 0'
        elif _class == 'city':
            line = f'{fname}, 0, 0, 1'
        with open(PATH, 'a') as file:
            file.write('\n')
            file.write(line)
