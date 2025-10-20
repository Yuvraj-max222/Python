# Program to store lines with average marks > 65 into a new file
def filter_students(input_file, output_file):
    with open(input_file, 'r') as infile, open(output_file, 'w') as outfile:
        for line in infile:
            parts = line.strip().split()
            if not parts:
                continue
            student_id = parts[0]
            marks = list(map(int, parts[1:]))
            avg = sum(marks) / len(marks)
            if avg > 65:
                outfile.write(line)
input_file = "students.txt"
output_file = "selected.txt"
filter_students(input_file, output_file)
print("Filtered data written to", output_file)