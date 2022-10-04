import time

start = time.time()

# commanda = ''

startNumberRecord = 1
startIndex = 1
lastIndex = 170
# '''


nameFiles=("result_vars_input.txt",
           "result_vars_output.txt",
           "result_fill_handles_i.txt",
           "result_fill_handles_o.txt",
           "result_read_in_vars.txt",
           "result_read_outvars_from_asrv.txt",
           "result_writeout_vars.txt")

listRead = [[], [], [], [], [], [], []]
listWrite = []


def readFile(name_file: str, index: int):
    f = open('Templates/' + name_file, 'r', encoding="utf-8")
    # f = open('Templates/' + name_file, 'r', encoding="ASCII")
    for row in f:
        # print(row, end='')
        listRead[index].append(row)
    f.close()
    # print("\nStream ->", f.closed)
    return 0


def writeFile(name_file: str, counter: int, index: int, cmd: str, numRecord: int):
    string = ""
    numVlv: str = str(counter)

    symbol_limit: int = 4
    temp_number: str = str(numRecord)
    number_record: str = "0" * (symbol_limit - len(temp_number)) + temp_number

    f = open('Created/' + name_file, cmd, encoding="utf-8")
    for i in range(0, len(listRead[index])):
        # print(list[i],end="")
        # point = list[i].find('<LabelIn>')
        # print('\n',point,'\n',len('<LabelIn>'))
        # string = list[i].replace('<LabelIn>', LabelIn)
        string = listRead[index][i]
        string = string.replace('<numVlv>', numVlv)
        string = string.replace('<NumberRecord>', number_record)
        # string = string.replace('<tag_In>', tag_In)
        # string = string.replace('<Var_In>', Var_In)
        # string = string.replace('<Description>', description)
        # print(string)
        # list[i] = string
        f.write(string)
    # f.write('\n')
    # string = input('\nEnter data: ')
    # print(string.isalpha())
    f.close()

    return 0


def main():
    # global startIndex, lastIndex
    counter: int = startIndex
    numberRecord: int = startNumberRecord

    for i in range(len(nameFiles)):
        # listRead.append()
        readFile(nameFiles[i], i)

    while counter <= lastIndex:
        if counter == startIndex:
            command = 'w'
        else:
            command = 'a'

        # numVlv = str(counter)
        # tag_In = tag_In_Initial + numVlv + tag_In_End
        # tag_Out = tag_Out_Initial + numVlv + tag_Out_End

        for i in range(len(nameFiles)):
            writeFile(nameFiles[i], counter, i, command, numberRecord)
            listWrite.clear()

        counter += 1
        numberRecord += 1


if __name__ == "__main__":
    main()

    end = time.time()
    print(f"Time to complete threading read/writes: {round(end - start, 2)} seconds")
    





    

    



