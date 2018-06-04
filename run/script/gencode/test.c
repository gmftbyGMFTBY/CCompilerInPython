int main() {
    int a;
    a = 1;
    a = a * 2 + 3 * (8 - 6);
    a = fool(a, 2 + 3);
    return a;
}

int fool(int a, int b) {
    return a + b;
}
