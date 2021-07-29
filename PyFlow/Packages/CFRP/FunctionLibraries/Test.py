# class A:
#     def __init__(self):
#         self.name = 12
#         self.aaaa = 333
#
#     def number(self):
#         print(122133)
#
# class B(A):
#     def __init__(self):
#         super().__init__()
#         self.a=A()
#
#     @staticmethod
#     def happy(h):
#         h.number()
#
#
# b=B()
# B.happy(b)

# creating an instance to be able to call dosomethingelse(),or you may use any existing instace a=test2() a.dosomethingelse() def dosomethingelse(self): print "do something else" test2.dosomething()



# class Tester:
#     a=A()
#
#     def local(self):
#         print("I'm a local!")
#
#     @staticmethod
#     def another_stat():
#         A.number(self=a)
#         print("I'm a static!")
#
#     @staticmethod
#     def stat(inst):
#         inst.local()
#
#
# Tester.another_stat()
# t = Tester()
# Tester.stat(t)

# Out:

# I'm a local!

# I'm a static!

# Normal method:

class Myclass:
    def normal_method(self, data):
        print("Normal method called with instance %s and data %s" % (self, data))

    @classmethod
    def class_method(cls, data):
        print("Class method called with class %s and data %s" % (cls, data))

    @staticmethod
    def static_method(data):
        print("Static method called with data %s" % (data))

