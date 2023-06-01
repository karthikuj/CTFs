# Solution

## URL
- [RustScan](https://tryhackme.com/room/rustscan)

## Steps

### Task 5:
#### What is the scripting file config called?
1. The answer is `rustscan_scripts.toml`.

#### Can you run other binaries with RustScan? (T)rue / (F)alse.
1. The answer is `T`.

#### Can you run other binaries with RustScan? (T)rue / (F)alse.
1. The answer is `F`.

### Task 7:
#### Try running the scan for all ports.
1. To run a scan on all ports do this: `rustscan -a 10.10.59.239 -r 1-65535 -- -A | tee rustscan.txt`.

#### After scanning this, how many ports do we find open under 1000?
1. The answer is `2`.

#### Perform a service version detection scan, what is the version of the software running on port 22?
1. The answer is `6.6.1p1`.

#### Perform an aggressive scan, what flag isn't set under the results for port 80?
1. The answer is `httponly`.

### Task 8:
#### First, how do you access the help menu?
1. The answer is `-h`.

#### Often referred to as "quiet" mode, What switch can do this?
1. The answer is `-q`.

#### Which switch can help us to scan for a particular Range?
1. The answer is `-r`.

#### What switch would you use to find out RustScan's version?
1. The answer is `-v`.

#### Which switch will help us to select batch size?
1. The answer is `-b`.

#### Which switch can set timeout?
1. The answer is `-t`.
