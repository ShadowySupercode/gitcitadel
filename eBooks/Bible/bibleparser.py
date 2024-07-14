import re
import sys
filename = sys.argv[1]
pattern_chapter  = '(.*) (Chapter [0-9]{1,4})(.*)?'
pattern_verse = '([0-9]{1,4}):([0-9]{1,4})\. (.*)?'
book = ""

# Make sure file gets closed after being iterated
with open(filename, 'r') as f:
   # Read the file contents and generate a list with each line
   lines = f.readlines()

new_file = ""
current_chapter = "undef"

# Iterate each line
for line in lines[1:]:

    # Regex applied to each line    
    match = re.match(pattern_chapter, line)
    if match:
        book = match.group(1)
        chapter_text = f"{book} {match.group(2)}"
        # Make sure to add \n to display correctly when we write it back
        new_line = f"\n\n## {chapter_text}\n\n### {chapter_text}:Introduction\n"
        print(new_line)
        new_file += new_line
        current_chapter = chapter_text
        continue

    # Regex applied to each line 
    match = re.match(pattern_verse, line)
    if match:
        # Make sure to add \n to display correctly when we write it back
        new_line = f"\n\n### {current_chapter}:{match.group(2)}\n{match.group(3)} "
        print(new_line)
        new_file += new_line
        continue

    new_file += line.strip().replace("\n"," ")+" "

new_file = f"{lines[0]}\n## {book} Introduction\n" + new_file

newfilename = "/home/stella/Documents/Books/Bible/Completed/"+filename

with open(newfilename, 'w') as f:
     # write the lines
     f.write(new_file)