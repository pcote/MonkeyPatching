class MyClass(object):
    def __init__(self, msg):
        self.msg = msg

    def say_stuff(self):
        print("Say stuff message is: {}\n\n".format(self.msg))


# normal call and instantiation
ob1 = MyClass("Hello there, first example.")
ob1.say_stuff()


# "self" really isn't that special
class MyClass(object):
    def __init__(her, msg):
        her.msg = msg

    def say_stuff(her):
        print("Say stuff message is: {}\n\n".format(her.msg))

# normal call and instantiation
ob1 = MyClass("Hello there, This is me.")
ob1.say_stuff()


# Rearrange the call to show relationship between class and instance explicitly.
say_stuff = MyClass.say_stuff
say_stuff(ob1)


# Place the instance and method in separate classes.
class MyClass(object):
    def say_stuff(self):
        print("Say stuff message is: {}\n\n".format(self.msg))


class OtherClass(object):
    def __init__(self, msg):
        self.msg = msg


other_ob = OtherClass("Hello there, folks. This is the other_ob instance")
MyClass.say_stuff(other_ob)


# Working without an init with attribute setting instead of another class.
class MyClass(object):
    def say_stuff(self):
        print("Say stuff message is: {}\n\n".format(self.msg))

ob = MyClass()
setattr(ob, "msg", "Here is a message from a set attribute")
ob.say_stuff()


# Patching both the class and it's instance.
class MyClass(object):
    pass

ob = MyClass()

def say_stuff(self):
    print("The say stuff message here is: {}\n\n".format(self.msg))

setattr(MyClass, "say_stuff", say_stuff)
setattr(ob, "msg", "here is another patched in message to go with the patched in class")
ob.say_stuff()

#Do the same kind of patch job but with direct dictionary access instead. (to the instance)
class MyClass(object):
    pass

ob = MyClass()

def say_stuff(self):
    print("The say stuff message here is: {}\n\n".format(self.msg))

setattr(MyClass, "say_stuff", say_stuff)

ob.__dict__["msg"] = "Here is a message that gets set via the instance dictionary"
ob.say_stuff()

# Note: No You may not do a direct __dict__ on a class because that dictionary is a "mappingproxy" and won't let you do it that way.
# Metaprogramming zone here????


# Let's now take a method and replace it with a new one.
class MyClass(object):
    def __init__(self, msg):
        self.msg = msg

    def say_stuff(self):
        print("My standard say stuff message is: {}\n\n".format(self.msg))

def say_other_stuff(self):
    print("The new version of say_stuff says it like this: {}\n\n".format(self.msg))

MyClass.say_stuff = say_other_stuff

ob = MyClass("This is my message here")
ob.say_stuff()

# Let's outright ignore a class method and make up our own.
class MyClass(object):
    def __init__(self, msg):
        self.msg = msg

    def say_stuff(self):
        print("My standard say stuff message is: {}\n\n".format(self.msg))

ob = MyClass("Here is the original message")

def say_stuff():
    m = "Surprise!!! You thought I was going to say something else, didn't you?"
    print(m)

#setattr(ob, "say_stuff", say_stuff)
ob.__dict__["say_stuff"] = say_stuff

ob.say_stuff()

# THE END