from process_list import process_list

numbers = [1, 2, 1, 2, 3, 2]

if __name__ == "__main__":
    averages = process_list(numbers)
    print(numbers)
    print('Averages')
    print(averages)


for i in range(100):
    averages = process_list(averages)
    print(averages)
