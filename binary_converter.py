def converter():
    """Decimal-binary converter"""
    while True:
        number_input = input("Enter a number to convert, space and: \
        \n'2' if you want to convert binary number into decimal \
        \n'10' if you want to convert decimal number into binary \
        \n(or a letter to quit)")

        if (number_input[:-3].isdigit() and number_input[-3:] == " 10" or  # Check if the input is valid.
                all(i in "01" for i in number_input[:-2]) and number_input[-2:] == " 2"):

            conversion_type = int(number_input.split(" ")[1])  # Split the number and conversion type from input.
            number = number_input.split(" ")[0]

            if conversion_type == 2:  # Binary to decimal
                reversed_number = number[-1::-1]
                decimal = 0
                for i in range(len(reversed_number)):
                    item = int(reversed_number[i]) * 2 ** i
                    decimal += item

                result = str(decimal)
                conversed = "10"

            elif conversion_type == 10:  # Decimal to binary
                number = int(number)
                binary_list = []
                while True:
                    single_sign = number % 2
                    binary_list.append(single_sign)
                    if number == 0 or number == 1:
                        break
                    number //= 2
                binary_list = list(reversed(binary_list))
                binary = "".join(map(str, binary_list))

                result = binary
                conversed = "2"

            s1 = ("/-" + "-" * len(result) + "---" + "-" * len(conversed) + "-\\\n")
            s2 = ("| %s | %s |\n" % (result, conversed))
            s3 = ("\\-" + "-" * len(result) + "---" + "-" * len(conversed) + "-/\n")
            print(s1 + s2 + s3)

        elif number_input.isalpha():
            break

        else:
            print("Invalid input. Try again.")


converter()
