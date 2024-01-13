def announce(f):
    def wrapper():
        print("before ... ")
        f()
        print("after.")
    return wrapper

@announce
def hello():
    print("hello world.")

hello()
