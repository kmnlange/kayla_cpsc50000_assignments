def open_file(filename):
    print(f'Print from {filename} ******')
    rows = []
    try:
        with open(filename,'r') as file:
            for line_number, line in enumerate(file):
                line = line.strip()       # Removes the beginning and trailing spaces
                if line.startswith('#') or not line:
                    continue

                rows.append(line)

    except Exception as e:
        print(f'oops--we have an error with the file. \n The error is {e}')

    return rows

def main():
    filename = 'gradebook_demo.txt'
    rows = open_file(filename)
    # The Pythonic way of opening a file

    for row_number, row in enumerate(rows):
        cols = line.split(',')
    print(repr(line))
    print(cols)

    print(f'First name: {cols[6]}')
    print()

    main()
 
# Ava,Johnson,Computer Science,CS101,Intro to Programming,fa2024,3.7
        
gpa = float(cols[6])

        # unpacking a list
first_name, last_name, major, course_id, course_name, semester, gpa = cols

#except IndexError:
    #print('You are attempting to access an index that does not exist.')
#except ZeroDivisionError:
    #print('You are trying to divide by zero-- you cannot do that, dummy.')
except Exception as e:
    print(f'oops--we have an error with the file. \n The error is {e}')