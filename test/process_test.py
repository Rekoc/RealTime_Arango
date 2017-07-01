from multiprocessing import Process
import multiprocessing
import time

print('(Main) BEGIN process_test.py')

########
# Creation of one pipe between one process qnd the main program


def consumer(p1, p2):
    p1.close()  # Close producer's end (not used)
    while True:
        try:
            item = p2.recv()
        except EOFError:
            break
        print(item)


def producer(sequence, output_p):
    for item in sequence:
        output_p.send(item)
        time.sleep(0.1)

(p1, p2) = multiprocessing.Pipe()
cons = multiprocessing.Process(target=consumer, args=(p1, p2))
cons.start()

# Close the input end in the producer
p2.close()

# Go produce some data
sequence = range(100)
producer(sequence, p1)

# Close the pipe
p1.close()

#########
# Creation of 2 process


'''def count(n):
    while n > 0:
        n -= 1

tps1 = time.clock()
count(100000000)
count(100000000)
tps2 = time.clock()
print(tps2 - tps1)

tps3 = time.localtime()
p1 = Process(target=count, args=(100000000,))
p1.start()
p2 = Process(target=count, args=(100000000,))
p2.start()

p2.join()
p1.join()

tps4 = time.localtime()
print(tps4.tm_sec - tps3.tm_sec)'''

print('(Main) END process_test.py')