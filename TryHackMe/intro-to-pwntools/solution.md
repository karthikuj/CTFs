# Solution

## URL
- [Intro To Pwntools](https://tryhackme.com/room/introtopwntools)

## Steps

### Task 2:
#### Does Intro2pwn1 have FULL RELRO (Y or N)?
1. Enter these commands:
    ```
    checksec intro2pwn1
    checksec intro2pwn2
    ```
2. The answer is `Y`.

#### Does Intro2pwn1 have RWX segments (Y or N)?
1. The answer is `N`.

#### Does Intro2pwn2 have a stack canary (Y or N)?
1. The answer is `N`.

#### Does Intro2pwn2 not have PIE (Y or N)?
1. The answer is `Y`.

#### Cause a buffer overflow on intro2pwn1 by inputting a long string such as AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA. What was detected? 
1. The answer is `stack smashing`.

#### Now cause a buffer overflow on intro2pwn2. What error do you get?
1. The answer is `Segmentation fault`.

### Task 3:
#### Which user owns both the flag.txt and intro2pwn3 file?
1. Enter the command: `ls -al`.
2. The answer is `dizmas`.

#### Use checksec on intro2pwn3. What bird-themed protection is missing?
1. Run the command: `checksec intro2pwn3`.
2. The answer is `canary`.

#### What ascii letter sequence is 0x4a4a4a4a (pwndbg should tell you).
1. Run these commands:
    ```
    gdb intro2pwn3
    r < alphabet
    ```
2. Looking at the value of EIP, we can see it has been overwritten. Check its value.
3. The answer is `JJJJ`.

#### What is the output of "cyclic 12"?
1. Enter the command: `cyclic 12`.
2. The answer is `aaaabaaacaaa`.

#### What pattern, in hex, was the eip overflowed with?
1. Enter these commands:
    ```
    cyclic 100 > pattern
    gdb intro2pwn3
    r < pattern
    ```
2. Checking the value of EIP, we get our answer.
3. The answer is `0x6161616a`.

#### What is the flag?
1. Run these commands:
    ```
    python pwn_cyclic.py > attack
    ./intro2pwn3 < attack
    ```
2. Got the flag: `flag{13@rning_2_pwn!}`.

### Task 4:
#### What port is serving our challenge?
1. The answer is `1337`.

#### Please use checksec on serve_test. Is there a stack canary? (Y or N)
1. The answer is `Y`.

#### What is the flag?
1. Copy `task-4-poc.py` into the VM and run it.
2. Got the flag: `flag{n3tw0rk!ng_!$_fun}`.

### Task 5:
#### What does ASLR stand for?
1. The answer is `Addess Space Layout Randomization`.

#### Who owns intro2pwnFinal?
1. The answer is `root`.

#### Use checksec on intro2pwn final. Is NX enabled? (Y or N)
1. The answer is `N`.

#### Please use the cyclic tool and gdb to find the eip. What letter sequence fills the eip?
1. The answer is `taaa`.

#### Run your exploit with the breakpoint outside of gdb (./intro2pwnFinal < output_file). What does it say when you hit the breakpoint?
1. The answer is `Trace/breakpoint trap`.

#### Run the command "shellcraft i386.linux.sh -f a", which will print our shellcode in assembly format. The first line will tell you that it is running a function from the Unix standard library, with the parameters of "(path='/bin///sh', argv=['sh'], envp=0)." What function is it using?
1. The answer is `execve`.

#### Run whoami once you have the shell. Who are you?
1. After running `task-5-poc.py`, The answer is `root`.

#### What is the flag?
1. Run the command: `cat /root/flag.txt`.
2. Got the flag: `flag{pwn!ng_!$_fr33d0m}`.