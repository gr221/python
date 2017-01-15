
def fun(par, *args):
    print('par ist', par)
    i = 0
    for a in args:
        print('var.parameter', i, 'ist', a)
        i = i + 1


fun("foo", "bar", "baz", "blubb")
