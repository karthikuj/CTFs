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

### Task 5:
#### What is the value of var_8h on the second iteration of the loop?
1. Run the command `r2 -d loop2` to debug the binary.
2. Run the command `aaa` to analyze the binary.
3. Run the command `afl` to list all functions in the binary.
4. Run the command `e asm.syntax=intel` to change the assembly syntax to intel.
5. Run the command `pdf @main` to print the disassembled main function.
6. Set a breakpoint on `cmp` instruction with the command `db 0x560e5cb7862f`.
7. Continue execution till breakpoint using `dc` command.
8. Since we need to be in second iteration of the loop, we can run `dc` 2 more times.
9. Now we can print the value of `var_8h` using `px @rbp-0x8`.
10. The answer is `5`.

#### What is the value of var_ch on the second iteration of the loop?
1. Run the command `px @rbp-0xc`.
2. The answer is `0`.

#### What is the value of var_8h at the end of the program?
1. Set a breakpoint after the loop is finished using `db 0x560e5cb78635`.
2. List all breakpoints with command `db`.
3. Remove the previous breakpoint with `db- 0x560e5cb7862f`
4. Now continue execution till breakpoint using `dc`.
5. Print the value of `var_8h` using the command `px @rbp-0x8`
6. The answer is `2`.

#### What is the value of var_ch at the end of the program?
1. Run the command `px @rbp-0xc`.
2. The answer is `0`.

### Task 6:
#### What is the password?
1. Run the command `r2 -d crackme1` to debug the binary.
2. Run the command `aaa` to analyze.
3. Run the command `afl` to list all the functions.
4. Run the command `e asm.syntax=intel` to set the assembly syntax to intel.
5. Run the command `pdf @main` to print disassembled main function.
6. We can see that strcmp is being called, must be to check the equality of the actual password and the password we give.
7. Above strcmp call some values are being moved to `rsi` and `rdi` registers, which usually hold the first and second arguments in function calls.
8. Set breakpoint on strcmp call using the command `db 0x5568db8e18a4`.
9. Continue the execution till breakpoint using `dc` command.
10. When prompted for password, enter anything.
11. Check the values of registers using `dr`.
12. This will only show you memory address.
13. To check the values run the command: `px @rsi` and `px @rdi`.
14. You will notice that `rdi` holds the password we gave and `rsi` has a string `127.0.1`.
15. `127.0.1` did not work as a password, but using our intuition we can figure that the password is `127.0.0.1`.

### Task 7:
#### What is the correct password?
