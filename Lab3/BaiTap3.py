#Write a program that makes a backup of a file. Your program should
#prompt the user for the name of the file to copy and then write a new file
#with the same contents but with .bak as the file extension

filename = input('Which file would you like to back-up? ')
new_filename = filename + '.bak'
backup = open(new_filename, 'w')
for line in open(filename):
    backup.write(line)
    backup.close()
