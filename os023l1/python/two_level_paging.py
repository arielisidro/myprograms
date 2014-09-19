__author__ = 'ariel'


def convert_to_binary(number):

    print ("number: ",number)
    b = ""
    while number > 0:
        b = str(number % 2) + b
        number = int(number / 2)

    print ("binary ", b)

    return b


def convert_to_decimal(s):

    d = 0
    l = len(s)
    y = 0
    i = l
    while i > 0:

        d += int(s[i-1:1]) * 2**y
        y += 1

    return d


def pad_left(s):

    return (32-len(s))*'0'+s


def main():

    address = long(raw_input("Please input logical address: "))

    print("Address : ", address)

    binary = convert_to_binary(address)
    binary = pad_left(binary)

    print(binary)
    p1 = binary[0:12]
    p2 = binary[12:22]
    d = binary[22:32]

    print("p1 : ", p1)
    print("p2 : ", p2)
    print(" d : ", d)
    print("p1 : ", convert_to_decimal(p1))
    print("p2 : ", convert_to_decimal(p2))
    print(" d : ", convert_to_decimal(d))



if __name__ == '__main__':
    main()