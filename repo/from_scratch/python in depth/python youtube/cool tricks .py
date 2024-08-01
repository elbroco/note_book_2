# STRING MULTILINE

# print(
#     """

#       HOLA HAHAHA
#       SD
#       DG
#       TT

#       """
# )

# -------------------


# PRINT USING FUNCTIONS

# NAME = "PEDRO"
# print(NAME.lower())
# print("PE" in NAME)

# -------------------

# escape for quotes
# print("el \"tipo\" y la 'tipa'")

# ---------------------

# using global function

# any
# true if one of the values is true

# book_1_read = True
# book_2_read = False

# read_any_book = any([book_1_read, book_2_read])

# print(read_any_book)

# all  true if all of the values are true

# ingredients = True
# meal = False

# ready_to_serve = all([ingredients, meal])

# print(ready_to_serve)

# ------------------------

# some built in functions

# abs() returns absolute value
# round() rounds to the nearest integer
# and also helps to put x amount of decimals

# -----------------------

# ENUMS
# from enum import Enum


# class State(Enum):
#     INACTIVE = 0
#     ACTIVE = 1


# print(State.ACTIVE)

# -----------------------

# control statements

# condition = True

# if condition == True:
#     print("the condition")
#     print("was true")

# -----------------------

# dogs = ["roger", 1, "syd", True]

# print("syd" in dogs)

# print(dogs[0])

# # updating list item
# dogs[2] = "billy"

# print(dogs)

# # extending a list

# dogs += ["richi", "bob", 4]

# print(dogs)


# ------------------

# variable scope

# def test():
#     age = 8
#     print(age)


# #print(age) this will raise an error
# test()

# --------------------

# nested functions


# def talk(phrase):
#     def say(word):
#         print(word)

#     words = phrase.split(" ")
#     for word in words:
#         say(word)


# talk("i am going to the milk")

# --------------------

# nonlocal (variable scope)


# def count():
#     count = 0

#     def increment():
#         nonlocal count
#         count = count + 1
#         print(count)

#     increment()


# count()

# ---------------------

# loops and index

# items = [1, 2, 3, 4, 5, "julio", True]

# for index, item in enumerate(items):
#     print(index, item)


# ---------------------

# continue


# items = [1, 2, 3, 4, 5, "julio", True]

# for i in items:
#     if i == 4:
#         continue
#     print(i)
