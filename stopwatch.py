# Dibuat Oleh : Revan Kautsar Mulyana 
# Tanggal     : 07-01-2025
# PROJECT100
import time

print("Simple Stopwatch")

start_time = 0
end_time = 0
elapsed_time = 0
running = False

while True:
    print("\n1. Start")
    print("2. Stop")
    print("3. Reset")
    print("4. Quit")
    
    choice = input("Choose an option: ")
    
    if choice == "1":
        start_time = time.time()
        running = True
        print("Stopwatch started.")
        
    elif choice == "2":
        if running:
            end_time = time.time()
            elapsed_time += end_time - start_time
            running = False
            print("Stopwatch stopped.")
        else:
            print("Stopwatch is not running.")
            
    elif choice == "3":
        start_time = 0
        end_time = 0
        elapsed_time = 0
        running = False
        print("Stopwatch reset.")
        
    elif choice == "4":
        if running:
            print("Stopwatch is still running. Please stop or reset.")
        else:
            print(f"Total elapsed time: {elapsed_time:.2f} seconds")
            break
            
    else:
        print("Invalid option. Please choose again.")
        
    if not running and elapsed_time > 0:
        print(f"Elapsed time: {elapsed_time:.2f} seconds")