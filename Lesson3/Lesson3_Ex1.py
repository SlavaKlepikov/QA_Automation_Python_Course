data = input("Please write a single line\n")
revers_str = data[::-1]
print(revers_str)
replace_text = data.replace("bad","good")
print(replace_text)
count_occurrences = (data.count("bad"))
print(f"Have been made {count_occurrences} replacements")

