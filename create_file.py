leetcode_name = input("Enter Name of Problem: ")
actual_file_name = leetcode_name.replace(".", "").replace(" ", "_").lower()

file_type = "python"    # input("Enter Type [options: java / python / pandas]: ").lower()
if file_type == "java":
    actual_file_name = "Java/" + actual_file_name + ".py"
elif file_type == "python":
    actual_file_name = "python/" + actual_file_name + ".py"
elif file_type == "pandas":
    actual_file_name = "python/30_days_of_pandas/" + actual_file_name + ".py"
else:
    raise ValueError("Invalid type of file!")

with open(actual_file_name, "x") as f:
    print("Created file at " + actual_file_name)