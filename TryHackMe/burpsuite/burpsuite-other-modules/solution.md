# Solution

## URL
- [BurpSuite Other Modules](https://tryhackme.com/room/burpsuiteom)

## Steps

### Task 3:
#### What is the base64 encoded version of this text?
1. Putting `Let's Start Simple` in decoder and encoding it as base64 we get `TGV0J3MgU3RhcnQgU2ltcGxl`.

#### What is the plaintext returned?
1. Putting `%4e%65%78%74%3a%20%44%65%63%6f%64%69%6e%67` in decoder and decoding it as URL we get `Next: Decoding`.

#### What is the decoded text?
1. Putting `&#x25;&#x33;&#x34;&#x25;&#x33;&#x37;` in decoder and smart decoding it we get `47`.

#### What is the final string?
1. Putting `Encoding Challenge` in decoder and encoding it into base64 we get `RW5jb2RpbmcgQ2hhbGxlbmdl`.
2. Further encoding that into ASCII Hex we get `5257356a62325270626d6367513268686247786c626d646c`.
3. Further encoding that into octal we get `24034214a720270024142d541357471232250253552c1162d1206c`.

### Task 4:
#### Convert this into an ASCII Hex string for the answer to this question.
1. Putting `Let's get Hashing!` in decoder and hashing it with SHA-256 and further encoding it with ASCII Hex we get `6b72350e719a8ef5af560830164b13596cb582757437e21d1879502072238abe`.

#### Generate an MD4 hashsum of the phrase: Insecure Algorithms. Encode this as base64 (not ASCII Hex) before submitting.
1. Putting `Insecure Algorithms` in decoder, hashing it as MD4 and further encoding it as base64 we get `TcV4QGZZN7y7lwYFRMMoeA==`.

#### "Some joker has messed with my SSH key! There are four keys in the directory, and I have no idea which is the real one. The MD5 hashsum for my key is 3166226048d6ad776370dc105d40d9f8 -- could you find it for me?"
1. Download the task files.
2. Unzip and cd into the new directory.
3. Run `md5sum * | grep 3166226048d6ad776370dc105d40d9f8` and you will the answer: `key3`.