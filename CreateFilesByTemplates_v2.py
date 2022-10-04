import time

start = time.time()

# commanda = ''



startNumberRecord = 57
startIndex = 2
lastIndex = 40
# '''


nameFiles=("result_vars_input.txt",
           "result_vars_output.txt",
           "result_fill_handles_i.txt",
           "result_fill_handles_o.txt",
           "result_read_in_vars.txt",
           "result_read_outvars_from_asrv.txt",
           "result_writeout_vars.txt")

listRead = []
listWrite = []


def readFile(name_file: str, index: int):
    f = open('Templates/' + name_file, 'r', encoding="utf-8")
    for row in f:
        # print(row, end='')
        listRead[index].append(row)
    f.close()
    # print("\nStream ->", f.closed)
    return 0


def writeFile(name_file: str, index: int, cmd: str):

    f = open('Created/' + name_file, cmd, encoding="utf-8")
    for i in range(0, len(listWrite[index])):
        f.write(listWrite[index][i])
    f.close()

    return 0


def main():
    # global startIndex, lastIndex
    # counter: int = startIndex
    # numberRecord: int = startNumberRecord

    for i in range(len(nameFiles)):
        listRead.append([])
        listWrite.append([])

        readFile(nameFiles[i], i)

        counter: int = startIndex
        numberRecord: int = startNumberRecord

        while counter <= lastIndex:
            numVlv: str = str(counter)

            symbol_limit: int = 4
            temp_number: str = str(numberRecord)
            number_record: str = "0" * (symbol_limit - len(temp_number)) + temp_number
            for j in range(0, len(listRead[i])):
                string = listRead[i][j]
                string = string.replace('<numVlv>', numVlv)
                string = string.replace('<NumberRecord>', number_record)
                listWrite[i].append(string)

            counter += 1
            numberRecord += 1

        writeFile(nameFiles[i], i, "w")
        # listWrite.clear()


if __name__ == "__main__":
    main()

    end = time.time()
    print(f"Time to complete threading read/writes: {round(end - start, 2)} seconds")
    





    

    



