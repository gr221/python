

def fun(par, *args, **kwargs):
    print('par ist', par)
    i = 0
    for a in args:
        print('var.parameter', i, 'ist', a)
        i = i + 1
    for key in kwargs:
        print("keyword parameter", key,
                'ist', kwargs[key])
    # als hätte ich definiert:
    # kwargs = { 'egon': 7,
    #        'november': 'kalt'}


fun("foo", "bar", "baz", "blubb",
        egon=7, november='kalt')
