def gun():
    print("In gun")
def run():
    print("In run")
    y()

def fun(x):
    print("In fun")
    x()

fun(run(gun))