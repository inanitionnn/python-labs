"""
lab3 variant 110
Tarasiuk Oleksandr
"""


def check(k):
    """
    checks if there are 2 in the
    ternary notation of a number
    """
    if k < 0:
        k = -k
    has_2 = False
    while k > 0 and not has_2:
        has_2 = (k%3)%2 == 0
        k //= 3
    return has_2


def answer(main_ln, main_ind, k):
    """
    writes the answer to the list

    main_ln - sequence length
    main_ind - sequence start index
    """
    answer = []
    if main_ln < 2:
        return answer
    while main_ln > 0:
        if check(k[main_ind]):
            answer.append(k[main_ind])
            main_ln -= 1
        main_ind += 1
    return answer


def first(cur_ind, cur_ln, k, last_ind, main_ind):
    """
    finds the first term
    """
    if check(k[cur_ind]):
        cur_ln = 1
        last_ind = cur_ind
        main_ind = last_ind
    return cur_ind, cur_ln, last_ind, main_ind


def search(k):
    """
    looks for the length and index of the
    first largest needed construct

    main_ln - sequence length
    main_ind - sequence start index
    last_ind - last term index
    cur_ln - current length
    cur_ind - current index
    state - sequence status flag
    spins - number of sequences
    main_ind2 - current start index
    """
    main_ind = None
    main_ln = 0
    last_ind = None
    cur_ln = 0
    cur_ind = 0
    state = 0
    spins = 0
    main_ind2 = None
    while cur_ind < len(k):
        if cur_ln == 0:  #find first term
            cur_ind, cur_ln, last_ind, main_ind = first(cur_ind, cur_ln, k, last_ind, main_ind)
            cur_ind += 1
            continue
        if check(k[cur_ind]):
            if state == 0 and k[last_ind] == k[cur_ind]:
                last_ind = cur_ind
                main_ind = last_ind
            elif state == 0 and k[last_ind] > k[cur_ind]:
                cur_ln += 1
                last_ind = cur_ind
                state = 1
            elif state == 1 and k[last_ind] >= k[cur_ind]: #the number increases
                cur_ln += 1
                last_ind = cur_ind
                if main_ln < cur_ln and spins == 0:
                    main_ln = cur_ln
                elif main_ln < cur_ln:
                    main_ln = cur_ln
                    main_ind = main_ind2
            elif (state == 1 or state == 2) and k[last_ind] <= k[cur_ind]: #the number falls
                cur_ln += 1
                last_ind = cur_ind
                state = 2
                if main_ln < cur_ln and spins == 0:
                    main_ln = cur_ln
                elif main_ln < cur_ln:
                    main_ln = cur_ln
                    main_ind = main_ind2
            elif state == 2 and k[last_ind] > k[cur_ind]: #the number increases and start new subsequence
                if main_ln < cur_ln and spins == 0:
                    main_ln = cur_ln
                elif main_ln < cur_ln:
                    main_ln = cur_ln
                    main_ind = main_ind2
                main_ind2 = last_ind
                cur_ln = 2
                last_ind = cur_ind
                spins += 1
                state = 1
        last_ind = cur_ind
        cur_ind += 1
    return main_ind, main_ln


def subsequence(k):
    """
    main function
    """
    main_ind, main_ln = search(k)
    result = answer(main_ln, main_ind, k)
    return result

