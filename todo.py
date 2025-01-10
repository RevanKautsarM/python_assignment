# Dibuat Oleh : Revan Kautsar Mulyana
# Tanggal     : 10-01-2025
# PROJECT 100
tasks = []
while True:
    task = input("Enter a task (or type 'done' to finish): ")
    if task.lower() == 'done':
        break
    tasks.append(task)
print("Your tasks:", tasks)
