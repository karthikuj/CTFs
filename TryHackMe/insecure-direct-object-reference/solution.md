# Solution

## URL:
- [IDOR](https://tryhackme.com/room/idor)

## Steps

### Task 1:
#### What does IDOR stand for?
1. The answer is: `Insecure Direct Object Reference`.

### Task 2:
#### What is the Flag from the IDOR example website?
1. Click `View Site`.
2. Check the emails to find the link: `https://onlinestore.thm/order/1234/invoice`
3. Change the number in URL to `1000`.
4. Got flag: `THM{IDOR-VULN-FOUND}`.

### Task 3:
#### What is a common type of encoding used by websites?
1. The answer is `base64`.

### Task 4:
#### What is a common algorithm used for hashing IDs?
1. The answer is `MD5`.

### Task 5:
#### What is the minimum number of accounts you need to create to check for IDORs between accounts?
1. The answer is `2`, duh.

### Task 7:
#### What is the username for user id 1?
1. Create an account.
2. Open the network tab and go to `Your Account` tab.
3. Notice a request going to `https://10-10-240-146.p.thmlabs.com/api/v1/customer?id=x`.
4. Copy this request as cURL.
5. Change the value of `id` param to `1`.
6. Send the request for the username: `adam84`.

#### What is the email address for user id 3?
1. In the cURL request we copied, change the value of the `id` param to `3`.
2. Send the request for the email address: `j@fakemail.thm`.