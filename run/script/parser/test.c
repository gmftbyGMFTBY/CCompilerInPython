int main() {
    int a;
    a = 1;
    a = a * 2 + 3 * (8 - 6);
    a = add(a, 2 + 3);
    return a;
}

int add(int a, int b) {
    return a + b;
}
