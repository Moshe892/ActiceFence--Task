
# the counter will help the program limit the user
# to 5 bad inputs only
count = 0

# the correct keys for opening the vault
key1 = 'abce1234'
key2 = 'bill3333'
key3 = 'john9876'

# a list which contains the 3 correct keys. when one of the keys
# has been entered, it will be deleted from the list
list1 = ['abce1234','bill3333','john9876']

def enterKey(try1, try2, try3):
    global count
    global list1
    #  removing the keys from the list, if entered by user
    if try1 in list1:
        list1.remove(try1)
    if try2 in list1:
        list1.remove(try2)
    if try3 in list1:
        list1.remove(try3)

    # get the number of items in the list, if 2 or more
    # items has been deleted from the list, access is given
    # if not, the program will add 1 bad entry to the counter
    l = len(list1)
    if l <= 1:
        print("access given")
    else:
        print("not enough correct keys entered!")
        count += 1
        print(f"--{5 - count} tries left")

    # after 5 bad entries, the vault will be sealed
    # the program will end
    if count >= 5:
        print("access denied!! Vault is now sealed")
        exit()

    # notify the user about the number of tries left



def getState():
    # in this function, each state has its own conditions

    # no item has been deleted from the list, and no bad entries
    # detected, which means the process hasn't been started yet
    if len(list1) == 3 and count == 0:
        print("Closed")
        return "Closed"

    # incorrect entries identified at least once, but still
    # not enough correct keys has entered. still in progress
    if len(list1) > 1 and 1 <= count <= 4:
        print("Unlock in progress")
        return "Unlock in progress"

    # 5 bad entries identified, therefore the vault now sealed
    if count >=5:
        print("Sealed")
        return "Sealed"

    # 2 or 3 correct keys has been entered, access given
    if len(list1) <= 1:
        print("Open")
        return "Open"

