int main() {
    int a;
    a = 1;
    a = a * 2 + 3;
    a = add(a, 2 + 3);
    return a;
}

int add(int a, int b) {
    return a + b;
}


/* 4-tuple, think that the first function is the main fucntion
    l1:     main
            D, _, _, a
            =, 1, _, a
            *, a, 2, a
            +, a, 3, a
            =, a, _, a
            =, 2, _, t1
            =, a, _, t2
            +, 2, 3, t3
            j, _, _, l2
            =, a, _, t1     // define that always use one paramter
            ret, _, _, _
    l2:     add - always use one paramter
            +, t1, t2, t1
            ret, _, _, _
 */
