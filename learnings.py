# To generate a string of numbers with space between them
# One line syntax

new_row=' '.join(str(1+i) for i in range(4))

# str(i+1) for i in range(4) => Gives a list of strings i.e. ['1','2','3','4']
# .join() functions joins each element by a space or empty string
