message = input('enter message to echoed: ')
count = input('enter number to echoed message number of times: ').strip()

if count:
    count = int(count)


    def echo_func(msg, cnt):
        while cnt > 0:
            print(msg)
            cnt -= 1


    echo_func(message, count)
