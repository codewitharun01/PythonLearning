name = "Arun"
greeting = "Hello, Arun"

print(greeting)

name = "James"

print(greeting)

greeting = f"Hello, {name}"
print(greeting)

# --

name = "Maya"
print(
    greeting
)  # This still prints "Hello, James" because `greeting` was calculated earlier.
print(
    f"Hello, {name}"
)  # This is correct, since it uses `name` at the current point in time.

# -- Using .format() --

# We can define template strings and then replace parts of it with another value, instead of doing it directly in the string.

greeting = "Hello, {}"
with_name = greeting.format("James")
print(with_name)

longer_phrase = "Hello, {}. Today is {}."
formatted = longer_phrase.format("James", "Monday")
print(formatted)