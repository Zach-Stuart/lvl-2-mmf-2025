# create file to hold data (add .txt extension)
file_name = "write_experiment"
write_to = "{}.txt".format(file_name)

text_file = open(write_to, "w+")

# strings to write to file
heading = "=== MMF Test ===\n"
content = "random content"
more = "more content? in this economy?"

# list of strings
to_write = [heading, content, more]

# print output
for item in to_write:
    print(item)

# write item to file
for item in to_write:
    text_file.write(item)
    text_file.write("\n")

