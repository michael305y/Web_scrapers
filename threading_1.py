import threading

def my_function():
    for i in range(5):
        print(f"Thread {threading.current_thread().name} - Count: {i}")

# Create two threads
thread1 = threading.Thread(target=my_function, name="Thread 1")
thread2 = threading.Thread(target=my_function, name="Thread 2")

# Start the threads
thread1.start()
thread2.start()

# Wait for both threads to finish
thread1.join()
thread2.join()

print("Both threads have finished.")





