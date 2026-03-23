# functions

# def hello():
#     print("hello how are u?")

# hello()
# hello()
# hello()

x = 500
def func():
    global x
    x = 200 # updates the global x
func()
print(x)