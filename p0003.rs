mod boilerplate;


fn main() {
    let mut i = 3;
    let mut n = 600_851_475_143;

    while n > 1 {
        if n % i == 0 {
            n = n / i;

        } else {
            i = loop {
                i += 2;

                if boilerplate::isprime(i) {
                    break i;
                }
            };

        }

    }

    println!("{i}");
}
