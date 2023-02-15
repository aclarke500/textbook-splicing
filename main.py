#import text
f = open("text.txt", "r")

sub_text = open("text_subset.txt", "w")

beginning_string = "sequences of bytes encoding the low-level"
ending_string = "microprocessors are among the most complex systems ever"

writing_mode = False

for i in f:

    if beginning_string in i:
        writing_mode = True

    if ending_string in i:
        writing_mode = False

    if writing_mode:
        sub_text.write(i)

f.close()
sub_text.close()

# get number of lines
f = open("text_subset.txt", "r")

chapter = f.readlines()

length = len(chapter)
print(length)
number_of_files=50

increment=int(length/number_of_files) # 20 files in current directory


current_line = 0


for i in range(number_of_files):
    file_name = "file" + str(i) + ".txt"
    file_idx = open(file_name, "w")

    for j in range(increment):
        file_idx.write(chapter[current_line])
        current_line+=1







