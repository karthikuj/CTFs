# Solution

## URL
- [Intro to Defensive security](https://tryhackme.com/room/defensivesecurity)

## Steps:
1. Open the SIEM.
2. Identiy the message in red (when you hover on it).
3. Take note of IP.
4. Check if it is malicious using the IP scanner they provided, in real world open-source databses such as AbuseIPDB or Cisco Talos Intelligence can be used.
5. Escalate the event to SOC team lead.
6. Block the IP in firewall.
7. Get the flag `THM{THREAT-BLOCKED}`.