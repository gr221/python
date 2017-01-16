def mittelwert(array):
    abs_value = 0
    for i in range(0, len(array)):
        abs_value = abs_value + array[i]

    mittelwert = abs_value / len(array)
    return mittelwert

def main():
    arr = [1,2,3,4,5,6]
    print(mittelwert(arr))

if __name__=="__main__":
    main()
