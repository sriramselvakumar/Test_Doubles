import sys

# Please check readme for instructions on how to run all this


def sum_up(file_name):

    try:
        f = open(file_name, 'r+')

        line = f.read()

        numbers = line.split(' ')

        result = 0

        for i in enumerate(numbers):

            numbers[i[0]] = int(i[1])

            result += numbers[i[0]]

        f.write(' ' + str(result))

        f.close()

    except FileNotFoundError:
        raise FileNotFoundError(file_name + 'was not found')

    except ValueError:
        f.close()
        raise ValueError('This program only sums up integers')


if __name__ == "__main__":
    sum_up('sum_test.txt')
