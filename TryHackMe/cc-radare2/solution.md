# Solution

## URL
- [CC: Radare2](https://tryhackme.com/room/ccradare2)

## Steps

### Task 2
#### What flag to you set to analyze the binary upon entering the r2 console (equivalent to running aaa once your inside the console)     
1. Enter the command `r2 -h`.
2. The answer is `-A`.

#### How do you enable the debugger?     
1. The answer is `-d`.

#### How do you open the file in write mode?
1. The answer is `-w`.

#### How do you enter the console without opening a file    
1. The answer is `-`.

### Task 3
#### What command "Analyzes Everything" (all functions and their arguments: Same as running with radare with -A)
1. Run the command `a?`.
2. Run the command `aa?`.
3. Run the command `aaa?`.
4. The answer is `aaa`.

#### What command does basic analysis on functions?
1. Run the command `a?`.
2. The answer is `af`.

#### How do you list all functions?
1. Run the command `af?`.
2. The answer is `afl`.

#### How many functions are in the example1 binary?
1. Run the command `afl`.
2. The answer is `12`.

#### What is the name of the secret function in the example1 binary?
1. Run the command `afl`.
2. The answer is `secret_func`.

### Task 4
#### What command shows all the information about the file that you're in?   
1. Run the command `i?`.
2. The answer is `ia`.

#### How do you get every string that is present in the binary? 
1. Run the command `iz?`.
2. The answer is `izz`.

#### What if you want the address of the main function?    
1. Run the command `i?`.
2. The answer is `iM`.

#### What character do you add to the end of every command to get the output in JSON format?
1. Run the command `i?`.
2. The answer is `j`.

#### How do you get the entrypoint of the file?
1. Run the command `i?`.
2. The answer is `ie`.

#### What is the secret string hidden in the example2 binary?    
1. Run the command `izz`.
2. The answer is `goodjob`.

### Task 5
#### How do you print out the the current memory address your located at in the binary?
1. Run the command `s?`.
2. The answer is `s`.

#### What command do you use to go to a specific point in memory with the syntax <command> <address>?
1. Run the command `s?`.
2. The answer is `s`.

#### What command would you run to go 5 bytes forward?
1. Run the command `s?`.
2. The answer is `s+ 5`.

#### What about 12 bytes backward?
1. Run the command `s?`.
2. The answer is `s- 12`.

#### How do you undo the previous seek?
1. Run the command `s?`.
2. The answer is `s-`.

#### How would go to the memory address of the main function?
1. Run the command `s?`.
2. The answer is `s main`. (r2 is actually showing the answer to be `sf main` but THM is not accepting that.)

#### What if you wanted to go to the address of the rax register?
1. Run the command `s?`.
2. The answer is `sr rax`.

### Task 6
#### How would you print the hex output of where you currently are in memory?
1. Run the command `p?`.
2. The answer is `px`.

#### How would you print the disassembly of where you're currently at in memory?
1. Run the command `p?`.
2. The answer is `pd`.

#### What if you wanted the disassembly of the main function?
1. Run the command `pd?`.
2. The answer is `pd @ main` (or `pdf @main`)

#### What command prints out the emoji hexdump? (this is not useful at all I just find it funny)
1. Run the command `px?`.
2. The answer is `pxe`.

#### What if you decided you were too good for rows and you wanted the disassembly in column format?
1. Run the command `p?`.
2. The answer is `pC`.

#### What is the value of the first variable in the main function for the example 3 binary?
1. Run the command `aaa` and `pdf @main`.
2. The answer is `1`.

#### What about the second variable?
1. Run the command `pdf @main`.
2. The answer is `5`.

### Task 7
#### How many functions are in the binary?
1. Run the command `aaa`.
2. Run the command `afl`.
3. The answer is `13`.

#### What is the value of the hidden string?
1. Run the command `izz`.
2. The answer is `you_found_me`.

#### What is the return value of secret_func()?
1. Run the command `pdf @sym.secret_func`.
2. The answer is `4`.

#### What is the value of the first variable set in the main function(in decimal format)?
1. Run the command `pdf @main`.
2. The answer is `12`.

#### What about the second one(also in decimal format)?
1. Run the command `pdf @main`.
2. The answer is `192`.

#### What is the next function in memory after the main function?
1. Run the command `pd @ main`.
2. The answer is `midterm_func`.

#### How do you get a hexdump of four bytes of the memory address your currently at?
1. Run the command `p?`.
2. The answer is `px 4`.

### Task 8
#### How do you set a breakpoint?
1. Run the command `d?`.
2. The answer is `db`. 

#### What command is used to print out the values of all the registers?
1. Run the command `d?`.
2. The answer is `dr`. 

#### How do you run through the program until the program either ends or you hit the next breakpoint?
1. Run the command `d?`.
2. The answer is `dc`. 

#### What if you want to step through the binary one line at a time?
1. Run the command `d?`.
2. The answer is `ds`. 

#### How do you go forth 2 lines in the binary?
1. Run the command `d?`.
2. The answer is `ds 2`. 

#### How do you list out the indexes and memory addresses of all breakpoints?
1. Run the command `db?`.
2. The answer is `dbi`.

### Task 9
#### How do you enter "graph mode" which allows everything to be organized in nice readable boxes?(A personal favorite of mine. Also note that the second character is uppercase)
1. Run the command `v?`.
2. The answer is `vV`.

#### What character do you press to run normal radare commands inside visual mode?
1. Enter visual mode using `v` and then enter `?`.
2. The answer is `:`.

#### How do you go back to the regular radare shell(leaving visual mode)?
1. Enter visual mode using `v` and then enter `?`.
2. The answer is `q`.

#### What if you want to step through the binary inside Visual mode?
1. Enter visual mode using `v` and then enter `?`.
2. The answer is `s`.

#### How do you add a comment?
1. Enter visual mode using `v` and then enter `?`.
2. The answer is `;`.

### Task 10
#### How do you write a string to the current memory address.
1. Run the command `w?`.
2. The answer is `w`.

#### What command lists all write changes?
1. Run the command `w?`.
2. The answer is `wc`.

#### What command modifies an instruction at the current memory address?
1. Run the command `w?`.
2. The answer is `wa`.

#### Get the example4 binary to show the You win! message
1. Run these:
    ```
    r2 -d example4
    aaa
    pdf @main
    db 0x559ef8e006bf
    dc
    wx 05 @ rbp-0x4
    dc
    ```

### Task 11
#### Congratulations on making it to this point. You should now be able to solve a crackme! Use all the tools you've learned and get that password! The binary to use for this task is the_final_exam!
1. Run the command `r2 -d the_final_exam`
2. Analyze the binary: `aaa`.
3. List the functions: `afl`.
4. Checkout the main finction: `pdf @ main`.
5. We can see that it takes an input and passes it to `sym.get_password` function and then it compares the output of `sym.get_password` to the string `youdidit`.
6. So we must pass some string to the binary that returns `youdidit`.
7. We can pass the string `youdidit` and evaluate the output.
8. Just when the 2 strings are compared read the arguments: `px @ rdi` and `px @ rsi`.
9. Now find the difference in their hex using this python script:

    ```py
    s1 = "83797f6e736e737e" # the output from sym.get_password
    s2 = "796f756469646974" # hex for "youdidit"

    difference = int(s1, 16) - int(s2, 16)

    print(f"The difference is: {hex(difference)}")
    ```
10. The difference is `a0a0a0a0a0a0a0a`.
11. Now we know that the `sym.get_password` function is adding that to the input. So, `hex(<password>) + 0xa0a0a0a0a0a0a0a = hex(youdidit)`.
12. Therefore, the hex of password must be: `hex(youdidit) - 0xa0a0a0a0a0a0a0a`.
13. Here's a python script for that:

    ```py
    passDec = int(s2, 16) - difference
    print(f"Hex of password is: {hex(passDec)}")
    ```
14. Now convert the hex to ASCII [here](https://www.rapidtables.com/convert/number/hex-to-ascii.html).
15. The password is: `oekZ_Z_j`.