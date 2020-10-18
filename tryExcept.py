# if u can anticipate the error that can occur in ur code,
# you can surround it with try except block and handle it however u want

try:
    pass
except Exception:
    pass

# FileNotFoundError:
# more generalised exception
#
# FileNotFoundError as e:
#     print(e)
# finally is executed evn if try throws an error, even when it doesnt,


try:
    f = open('curruptfile.txt')
    # if f.name == 'currupt_file.txt':
    #     raise Exception
except IOError as e:
    print('First!')
except Exception as e:
    print('Second')
else:
    print(f.read())
    f.close()
finally:
    print("Executing Finally...")

print('End of program')