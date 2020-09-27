
def choose_best_sum(t, k, ls):
    print("t:",t,"k:",k,"ls:",ls)
    ls2 = []
    while len(ls2) < k:
        for i in ls:
            print(ls2)
            if i > t:
                ls.remove(i)
            elif i <= t:
                ls2.append(i)
                t = t-i
            else:
                print("\n!!!else!!!\n")
    print(sum(ls2))
    return ls2

xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
choose_best_sum(230, 4, xs)
choose_best_sum(430, 5, xs)
choose_best_sum(430, 8, xs)

# Test.it("Bigger numbers")
# xs = [100, 76, 56, 44, 89, 73, 68, 56, 64, 123, 2333, 144, 50, 132, 123, 34, 89]
# Test.assert_equals(choose_best_sum(230, 4, xs), 230)
# Test.assert_equals(choose_best_sum(430, 5, xs), 430)
# Test.assert_equals(choose_best_sum(430, 8, xs), None)


"""t (maximum sum of distances, integer >= 0), k (number of towns to visit, k >= 1)
and ls (list of distances, all distances are positive or null integers and this
list has at least one element). The function returns the "best" sum ie the
biggest possible sum of k distances less than or equal to the given limit t,
if that sum exists, or otherwise nil, null, None, Nothing, depending on the
language. With C++, C, Rust, Swift, Go, Kotlin return -1."""
