
def checker(function):
    def checker(*args, **kwargs):
        try:
            result = function(*args, **kwargs)
        except Exception as exc:
            print(f"We have problems{exc}")
        else:
            print(f"No problems. Result - {result}")


    return checker


def calculate(expression):
    return  eval(expression)

calculate = checker(calculate)

calculate("2*2*3*240/2")
calculate("2*360*550*1000/5")
calculate("2*890*230*540*240/8")