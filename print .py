def switch_demo(arg):
    switche = {
        1: "One",
        2: "Two",
        3: "Three",
        4: "Four",
        5: "Five",
        6: "Six",
        7: "Seven",
        8: "Eight",
        9: "Nine",
        10: "Ten"
    }
    print switche.get(arg, "Invalid Input")
z=int(raw_input())
switch_demo(z)
