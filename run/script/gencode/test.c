int main() {
    int a;
    a = 1;
    a = a * 2 + 3 * (8 - 6);
    if (a > 1) {
        a = 1;
    }
    else {
        a = 2;
    }
    a = fool(a, 2);
    int b = 2;
    while ( b ) {
        if (b == 1) {
            a = a + 2;
        }
        else {
            a = a - 2;
            a = a + fool(1, 1);
        }
        b = b - 1;
    }
    return a;
}

int fool(int c, int d) {
    int w;
    int count;
    count = 0;
    for (w = 0; w <= c; w = w + 1) {
        count = count + d;
    }
    return count;
}
