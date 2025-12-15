# Rust fixme 1

![image.png](Rust%20fixme%201/image.png)

As a person that has never touch Rust before, I should refer to the hints

https://doc.rust-lang.org/book/ch01-03-hello-cargo.html

I see, so let’s try to build the project first, we can first use `cargo build` . In case cargo is not install, we can use `sudo apt install cargo`

```bash
cargo build                                                                                                                                                                                                                           
    Updating crates.io index
  Downloaded crossbeam-epoch v0.9.18
  Downloaded crossbeam-utils v0.8.20
  Downloaded crossbeam-deque v0.8.5
  Downloaded either v1.13.0
  Downloaded rayon-core v1.12.1
  Downloaded rayon v1.10.0
  Downloaded xor_cryptor v1.2.3
  Downloaded 7 crates (379.2KiB) in 0.57s
   Compiling crossbeam-utils v0.8.20
   Compiling rayon-core v1.12.1
   Compiling either v1.13.0
   Compiling crossbeam-epoch v0.9.18
   Compiling crossbeam-deque v0.8.5
   Compiling rayon v1.10.0
   Compiling xor_cryptor v1.2.3
   Compiling rust_proj v0.1.0 (Rust fixme 1/fixme1)
error: expected `;`, found keyword `let`
 --> src/main.rs:5:37
  |
5 |     let key = String::from("CSUCKS") // How do we end statements in Rust?
  |                                     ^ help: add `;` here
...
8 |     let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1", "61", "25", "7f", "5a", "60", "50", "11", "38", "1f", "3a", "60", "e9", "62", "20", "0c", "e6", "50", "d3", "35"];
  |     --- unexpected token

error: argument never used
  --> src/main.rs:26:9
   |
25 |         ":?", // How do we print out a variable in the println function? 
   |         ---- formatting specifier missing
26 |         String::from_utf8_lossy(&decrypted_buffer)
   |         ^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^ argument never used

error[E0425]: cannot find value `ret` in this scope
  --> src/main.rs:18:9
   |
18 |         ret; // How do we return in rust?
   |         ^^^ help: a local variable with a similar name exists: `res`

For more information about this error, try `rustc --explain E0425`.
error: could not compile `rust_proj` (bin "rust_proj") due to 3 previous errors

```

The correct code are the following, I just:

- Add `;` after the statement
- Use `return` to return
- Use `{}` for format string and print out the result

```rust
use xor_cryptor::XORCryptor;

fn main() {
    // Key for decryption
    let key = String::from("CSUCKS"); // How do we end statements in Rust?

    // Encrypted flag values
    let hex_values = ["41", "30", "20", "63", "4a", "45", "54", "76", "01", "1c", "7e", "59", "63", "e1", "61", "25", "7f", "5a", "60", "50", "11", "38", "1f", "3a", "60", "e9", "62", "20", "0c", "e6", "50", "d3", "35"];

    // Convert the hexadecimal strings to bytes and collect them into a vector
    let encrypted_buffer: Vec<u8> = hex_values.iter()
        .map(|&hex| u8::from_str_radix(hex, 16).unwrap())
        .collect();

    // Create decrpytion object
    let res = XORCryptor::new(&key);
    if res.is_err() {
        return; // How do we return in rust?
    }
    let xrc = res.unwrap();

    // Decrypt flag and print it out
    let decrypted_buffer = xrc.decrypt_vec(encrypted_buffer);
    println!(
        "{}", // How do we print out a variable in the println function? 
        String::from_utf8_lossy(&decrypted_buffer)
    );
}

```

After that, we can try to run `cargo build` once again, we can see it is successful

```bash
└─$ cargo build                                                                                                                                                                                                                           
   Compiling rust_proj v0.1.0 (Rust fixme 1/fixme1)
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.36s

```

Then get the flag after running the compiled executable, which is under `target/debug/`

```bash
└─$ ./target/debug/rust_proj                                                                                                                                                                                                              
picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}
```

We can also do this in one go without the use of `cargo build`, that is, to use `cargo run`

```bash
└─$ cargo run                                                                                                                                                                                                                             
    Finished `dev` profile [unoptimized + debuginfo] target(s) in 0.01s
     Running `target/debug/rust_proj`
picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}

```

Flag: `picoCTF{4r3_y0u_4_ru$t4c30n_n0w?}`