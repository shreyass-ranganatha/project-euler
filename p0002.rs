

fn main() {
    let (mut a, mut b) = (1, 1);
    let mut sm = 0;

    while b < 4_000_000 {
        if b % 2 == 0 {
            sm += b;
        }

        (a, b) = (b, a + b);
    };

    println!("{sm}");
}
