# Solution

## URL
- [Intro to x86-64](https://tryhackme.com/room/introtox8664)

## Steps

### Task 4:
#### What is the value of var_8h before the popq and ret instructions?
1. Run the command `r2 -d if2` to debug the `if2` executable.
2. Run the command `aaa` to analyze the executable.
3. Run the command `afl` to list the functions.
4. Run the command `e asm.syntax=intel` to set assembly syntax to intel.
5. Run the command `pdf @main` to disassemble and print the main function.
6. Set a breakpoint at `pop` instruction using the command `db 0x562c1ca0563c`.
7. Continue execution till breakpoint with the command `dc`.
8. At the top of the disassembled main function we have the address to `var_8h` which is `@rbp-0x8`.
9. Print its value using `px @rbp-0x8`.
10. The value is `60` in hexadecimal, which is `96` in decimal.
11. The answer is `96`.

#### what is the value of var_ch before the popq and ret instructions?
1. Print the value of `var_ch` using `px @rbp-0xc`.
2. The value is `0`.

#### What is the value of var_4h before the popq and ret instructions?
1. Print the value of `var_4h` using `px @rbp-0x4`.
2. The value is `1`.

#### What operator is used to change the value of var_8h, input the symbol as your answer(symbols include +, -, *, /, &, |):
1. In the disassembled code we can see the instruction `and dword [var_8h], 0x64`.
2. So the operator is `and` which can be symbolized as `&`.