def count_gap(x):
    """
        Perform Find the longest sequence of zeros between ones "gap" in binary representation of an integer

        Parameters
        ----------
        x : int
            input integer value

        Returns
        ----------
        max_gap : int
            the maximum gap length

    """
    try:
        # Convert int to binary
        b = "{0:b}".format(x)
        # Iterate from right to lift 
        # Start detecting gaps after fist "one"
        for i,j in enumerate(b[::-1]):
            if int(j) == 1:
                max_gap = max([len(i) for i in b[::-1][i:].split('1') if i])
                break
    except ValueError:
        print("Oops! no gap found")
        max_gap = 0
    return max_gap

print(count_gap(147))