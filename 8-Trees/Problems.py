def parenthesize(T, p):

    print(p.element(), end="")
    count = T.num_children(p)
    if not T.is_leaf(p):
        for child in T.children(p):
            if count == T.num_children(p):
                print("(", end="")
            count -= 1
            parenthesize(T, child)
            if count > 0:
                print(", ", end="")

        print(")", end="")
