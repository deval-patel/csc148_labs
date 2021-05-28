"""CSC148 Lab 4: Abstract Data Types

=== CSC148 Winter 2021 ===
Department of Mathematical and Computational Sciences,
University of Toronto Mississauga

=== Module Description ===
This module runs timing experiments to determine how the time taken
to enqueue or dequeue grows as the queue size grows.
"""
from timeit import timeit
from typing import List, Tuple
import matplotlib.pyplot as plt
from myqueue import Queue


###############################################################################
# Task 3: Running timing experiments
###############################################################################
def _setup_queues(qsize: int, n: int) -> List[Queue]:
    """Return a list of <n> queues, each of the given size."""
    # Experiment preparation: make a list containing <n> queues,
    # each of size <qsize>.
    # You can "cheat" here and set your queue's _items attribute directly
    # to a list of the appropriate size by writing something like
    #
    #     queue._items = list(range(qsize))
    #
    # to save a bit of time in setting up the experiment.
    # Make a list with <n> queues
    queue_list = [Queue() for _ in range(n)]

    # For each queue in <queue_list> make them have <qsize> items.
    for q in queue_list:
        q._items = [i for i in range(qsize)]

    return queue_list


def time_queue() -> None:
    """Run timing experiments for Queue.enqueue and Queue.dequeue."""
    # The queue sizes to try.
    queue_sizes = [10000, 20000, 40000, 80000, 160000]

    # The number of times to call a single enqueue or dequeue operation.
    trials = 200

    # This loop runs the timing experiment. Its three steps are:
    #   1. Initialize the sample queues.
    #   2. For each one, calling the function "timeit", takes three arguments:
    #        - a *string* representation of a piece of code to run
    #        - the number of times to run it (e.g. 1000)
    #        - globals is a technical argument that you DON'T need to care about
    #   3. Report the total time taken to do an enqueue on each queue.
    for queue_size in queue_sizes:
        queues = _setup_queues(queue_size, trials)
        time = 0
        for queue in queues:
            time += timeit('queue.enqueue(1)', number=1000, globals=locals())
        print(f'enqueue: Queue size {queue_size:>7}, time {time}')

    for queue_size in queue_sizes:
        queues = _setup_queues(queue_size, trials)
        time = 0
        for queue in queues:
            time += timeit('queue.dequeue()', number=1000, globals=locals())
        print(f'dequeue: Queue size {queue_size:>7}, time {time}')


def time_queue_lists() -> Tuple[List[int], List[float], List[float]]:
    """Run timing experiments for Queue.enqueue and Queue.dequeue.

    Return lists storing the results of the experiments.
    """
    # The queue sizes to try.
    queue_sizes = [10000, 20000, 40000, 80000, 160000]
    enqueue_times = []
    dequeue_times = []
    trials = 200

    for queue_size in queue_sizes:
        queues = _setup_queues(queue_size, trials)
        time = 0
        for queue in queues:
            time += timeit('queue.enqueue(1)', number=1000, globals=locals())
        print(f'enqueue: Queue size {queue_size:>7}, time {time}')
        enqueue_times.append(time)

    for queue_size in queue_sizes:
        queues = _setup_queues(queue_size, trials)
        time = 0
        for queue in queues:
            time += timeit('queue.dequeue()', number=1000, globals=locals())
        print(f'dequeue: Queue size {queue_size:>7}, time {time}')
        dequeue_times.append(time)

    return queue_sizes, enqueue_times, dequeue_times


if __name__ == '__main__':
    # Plot shit
    queue_sizes, enqueue_times, dequeue_times = time_queue_lists()
    plt.figure()
    plt.plot(queue_sizes, enqueue_times)
    plt.xlabel('Queue Sizes')
    plt.ylabel('Time')
    plt.suptitle('Enqueue times')
    plt.show()
    plt.figure()
    plt.plot(queue_sizes, dequeue_times)
    plt.suptitle('Dequeue times')
    plt.xlabel('Queue Sizes')
    plt.ylabel('Time')
    plt.show()
