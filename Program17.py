#Program to store lines with average marks > 65 into a new file
input_file = "marks.txt"
output_file = "selected_marks.txt"
with open(input_file, "r") as fin, open(output_file, "w") as fout:
    for line in fin:
        parts = line.strip().split()
        if not parts:
            continue
        student_id = parts[0]
        marks = list(map(int, parts[1:]))
        avg = sum(marks) / len(marks)
        if avg > 65:
            fout.write(line)