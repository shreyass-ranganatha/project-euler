

fn main() {
    let mut sm = 0;

    for i in 1..1000 {
        if (i % 5 == 0) || (i % 3 == 0) {
            sm += i;
        }
    }

    println!("{sm}");
}
