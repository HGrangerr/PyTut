name = "hello world"  # double quotes
place = 'mysore'  # single quote

new_name = "Bobby's world"
new_name = 'Bobby\'s world'

string_name = 'python for "beginners" '

# multiline

msgs = '''hi
hello
here'''

print(name, place, new_name, string_name, "\n", msgs)
# output:hello world mysore Bobby's world python for "beginners"  hi
# hello
# here


name.upper()  # wont work if not assigned back to string,not inplace,immutable
print(name) #Output:hello world

name = name.upper()  # works
print(name)

#HELLO WORLD


# single line comment

# multiline '''Python will ignore string literals that are not assigned to a variable, you can add a multiline string
# (triple quotes) in your code, and place your comment inside it:'''
# As long as the string is not assigned to a variable, Python will read the code, but then ignore it, and you have
# made a multiline comment

print(name[0])  #H
print(name[-1]) #D
print(name[-2]) #L

print(name[0:5])    #HELLO
print(name[:5])     #HELLO
print(name[6:])     #WORLD

# string slicing


no_of_o = name.count('o')   #0
index_of_s = place.find('s')        #2
print(no_of_o, index_of_s)

new_msg = name.replace('WORLD', 'UNIVERSE')
print(new_msg)
#HELLO UNIVERSE


concat_str = name + " ," + new_msg
print(concat_str)
#HELLO WORLD ,HELLO UNIVERSE

# string formatting
msg = '{},{},Welcome!'.format(name, concat_str)
# {} are called placeholders

message = f'{name},{concat_str.capitalize()},Welcome!'
print(message)     # HELLO WORLD,Hello world ,hello universe,Welcome!


print(msg)          # HELLO WORLD,HELLO WORLD ,HELLO UNIVERSE,Welcome!

print(len(msg))         # 48
print(dir(name))

print(help(concat_str.capitalize))
print(help(str))
