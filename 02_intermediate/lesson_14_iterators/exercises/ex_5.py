print(type(iter([1,2,3])))

print(type(iter("hello")))

# Explanation:
#
# iter([1,2,3])
#
# creates:
#
# list_iterator
#
# because Python built a special iterator for lists.
#
# iter("hello")
#
# creates:
#
# str_ascii_iterator
#
# because strings iterate character-by-character.
#
# Other examples:
#
# iter((1,2))
# → tuple_iterator
#
# iter({1,2})
# → set_iterator
#
# iter({"a":1})
# → dict_keyiterator