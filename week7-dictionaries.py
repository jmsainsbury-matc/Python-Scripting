#!/usr/bin/env python3

domains = {"server1.testlab.com":"192.168.1.10",
"server2.testlab.com":"192.168.1.11",
"server3.testlab.com":"192.168.1.12",
"server4.testlab.com":"192.168.1.13",
"server5.testlab.com":"192.168.1.14",
"server6.testlab.com":"192.168.1.15"}
print(domains.keys())
print(domains.values())
print(domains.items())

domains["server7.testlab.com"] = "192.168.1.16"
domains["server8.testlab.com"] = "192.168.1.17"


if "server2.testlab.com" in domains:
	print(domains.get("server2.testlab.com"))
if "server10.testlab.com" in domains:
	print(domains.get("server10.testlab.com"))
