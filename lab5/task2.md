## Task 2

1.  Most methods take longer to run on large inputs than on small inputs, although this is not always the case. Look at your code for your linked list method **len**. Do you expect it to take longer to run on a larger linked list than on a smaller one?

    Yes, I expect it to take longer on a larger linked list because I iterate through the entire linked list, and it is O(n) time, so as n gets larger, it will take more time.

2.  Pick one the following terms to relate the growth of \_\_len\_\_’s running time vs. input size, and justify.

    -   constant, logarithmic, linear, quadratic, exponential

    Linear

3.  Complete the code in time_lists.py to measure how running time for your **len** method changes as the size of the linked list grows.

    Compare this to the behaviour of calling len on a built-in list (the starter code begins this for you). What do you notice?

    I notice that the list's in built length is almost instant, however my LinkedList length is garabage.
