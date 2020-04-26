def test_argument(first_arg, *args):
    print("argument aval hast: ", first_arg)
    for arg in args:
        print("argument daroone args: ", arg)

test_argument('book', 'cat', '150', 50, 100.00056)        
