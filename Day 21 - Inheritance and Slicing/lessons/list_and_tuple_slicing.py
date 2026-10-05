# Day 21 Lesson: Python Slicing
#
# These examples come from the original Day 21 file.
#
# General slicing form:
#
# sequence[start:stop:step]
#
# The stop position is not included.


piano_keys = ["a", "b", "c", "d", "e", "f", "g"]
piano_tuple = ("do", "re", "mi", "fa", "so", "la", "ti")


print(piano_keys[2:5])
print(piano_keys[2:])
print(piano_keys[:5])
print(piano_keys[2:5:2])
print(piano_keys[::2])
print(piano_keys[::-1])
print(piano_tuple[2:5])
