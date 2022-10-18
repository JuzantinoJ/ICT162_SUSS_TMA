def main():
    x = [1, 2, 3] 
    try:
        print('begin try')
        index = int(input('Enter index: ')) 
        x[index] = 4
        print('end try')
    except Exception as e: 
        print('except block')
    else:
        print('else block')
    finally:
        print('finally block')
        print('end main')

# main()

def test():
    y = [1,2,3]
    ind = int(input('Enter index: '))
    y[ind] = 4
    print(y)
test()