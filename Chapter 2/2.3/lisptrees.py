from lisplists import *


def entry(tree):
    return car(tree)


def left_branch(tree):
    return cadr(tree)


def right_branch(tree):
    return caddr(tree)


def make_tree(entry_num, left, right):
    return makelist(entry_num, left, right)


def iselement_of_set(x, tree):  # tree represents the set
    if tree is None:
        return False
    elif x == entry(tree):
        return True
    elif x < entry(tree):
        return iselement_of_set(x, left_branch(tree))
    return iselement_of_set(x, right_branch(tree))


def adjoin_set(x, tset):
    if tset is None:
        return make_tree(x, None, None)
    elif x == entry(tset):
        return tset
    elif x < entry(tset):
        return make_tree(
            entry(tset),
            adjoin_set(x, left_branch(tset)),
            right_branch(tset)
        )
    return make_tree(
        entry(tset),
        left_branch(tset),
        adjoin_set(x, right_branch(tset))
    )


def tree_tolist1(tset):  # recursively converts the tree to list
    if tset is None:
        return None
    return append(tree_tolist1(left_branch(tset)),
                  cons(entry, tree_tolist1(right_branch(tset)))
                  )


def tree_tolist2(tset):  # iteratively converts tree to list

    def copy_tolist(tree, result_list):
        if tree is None:
            return result_list
        return copy_tolist(
            left_branch(tree),
            cons(entry(tree),
                 copy_tolist(right_branch(tree))
                 )
        )

    copy_tolist(tset, None)


def list_totree(elements):

    def partial_tree(elts, n):
        if n == 0:
            return cons(None, elts)
        else:
            left_size = int((n-1)/2)
            left_result = partial_tree(elts, left_size)
            left_tree = car(left_result)

            non_left_elts = cdr(left_result)

            right_size = int(n - (left_size + 1))
            this_entry = car(non_left_elts)
            right_result = partial_tree(cdr(non_left_elts), right_size)
            right_tree = car(right_result)
            remaining_elts = cdr(right_result)

            return cons(make_tree(this_entry, left_tree, right_tree),
                        remaining_elts
                        )

    return car(partial_tree(elements, length(elements)))


