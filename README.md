# ARP-Spoofer
A python Script to perform a MITM attack through ARP spoofing. It can also be used to DoS

# Usage

```bash
python3 ARPspoofer.py -t TARGET -a AP
```
![image](https://github.com/user-attachments/assets/73381271-7797-4412-b6fb-f01b40cdd017)

To rederict the traffic that gets to your machine you will need to execute the follwing commands

```bash
iptables --policy FORWARD ACCEPT
```
```bash
echo 1 > /proc/sys/net/ipv4/ip_forward
```
Appliyin the given filter,  you will see all the victim traffic

![image](https://github.com/user-attachments/assets/e86dcb45-e471-4683-9cdc-93519a04b3bf)

# Why it can be used as a DoS?

If you don't execute the previous commands, the traffic won't be redirected so it won't resolve.

![Imagen de WhatsApp 2024-12-29 a las 18 45 03_38cf3854](https://github.com/user-attachments/assets/cb3ea13f-7bcc-4017-8e9c-6376e2a6c63d)

📜 Disclaimer

This repository is intended for educational purposes only. The code provided here is designed to demonstrate concepts related to networking and protocols, such as ARP spoofing, for the purpose of learning and experimentation in a controlled and authorized environment.

The author is not responsible for any misuse of the code. Using these tools to attack or compromise networks or devices without explicit permission from the owners is illegal and may violate local, national, and international laws.
🚨 Legal Warning

    This code should only be used on networks where you have explicit permission to test and experiment.
    Ensure you have the explicit consent of the network administrators or device owners before conducting any tests.
    Do not use this code for malicious or illegal activities.

✅ Best Practices

    Use this repository only in controlled environments like test labs.
    Learn about cybersecurity ethically.
    Respect the laws of your country and the principles of the cybersecurity community.
