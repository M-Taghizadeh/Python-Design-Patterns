def test_argument_kw(**kwargs):
    if kwargs is not None:
        for key, value in kwargs.items():
            #print("{0} == {1}".format(key, value))
            print("%s == %s" % (key, value))

test_argument_kw(name = "pejman", age = "25", job = "engineer")
