ItemsInCart = 0

if ItemsInCart !=2:
    # raise Exception("Products cart count not matching")
    pass

assert(ItemsInCart == 0)


try:
    with open('text.txt', 'r') as r:
        r.read()
except:
    print("Somehow I reached this block because there is failure in try block")

try:
    with open('text.txt', 'r') as r:
        r.read()
except Exception as e:
    print(e)

finally:
    print("cleaning up resources")