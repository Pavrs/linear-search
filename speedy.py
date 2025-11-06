# [program name]
# Pavel Stoimenov
# [date]
# AS Computer Science

# [comment]
def one():
    try:
        #list
        nlist=[1, 2, 13, 14,17, 25]
        #counter
        finder= int(input('enter which number you want: '))
        found = False
        for x in nlist:
            #finder
            if  x == finder:
                found = True
                print('found')
                break
            else:
                print('not found')
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def two():
    try:
        pass   
    except Exception as e:
        print("Error occurred:", e )

# [comment]
def main():
    try:
        one()
        pass   
    except Exception as e:
        print("Error occurred:", e )    

if (__name__ == "__main__"):
    main()
