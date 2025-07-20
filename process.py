from multiprocessing import Process

def task1():
    print("Task 1 running")

def task2():
    print("Task 2 running")

#create processes
p1=Process(target=task1)       
p2=Process(target=task2)

#start processes
p1.start()
p2.start()

#wait for completion
p1.join()
p2.join()

print("Tasks Completed.")