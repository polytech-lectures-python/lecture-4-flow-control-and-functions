def scope_test():
    def local_assignment():
        msg = "local"

    def nonlocal_assignment():
        nonlocal msg
        msg = "nonlocal"

    def twice_nonlocal_assignment():
        # msg = 'inside twice nonlocal'
        def inner_fun():
            nonlocal msg
            msg = "twice nonlocal"
        inner_fun()

    def global_assignment():
        global msg
        msg = "global"

    msg = "test"
    local_assignment()
    print("After local assignment:", msg)
    nonlocal_assignment()
    print("After nonlocal assignment:", msg)
    twice_nonlocal_assignment()
    print("After twice nonlocal assignment:", msg)
    global_assignment()
    print("After global assignment:", msg)


scope_test()
# print("In global scope:", msg)
