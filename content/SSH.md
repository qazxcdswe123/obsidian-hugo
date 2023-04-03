---
aliases: []
date created: Nov 25th, 2022
date modified: Mar 29th, 2023
---

## Key Based Authentication
```
mkdir -p $HOME/.ssh
chmod 0700 $HOME/.ssh
```

Put public key into `.ssh/authorized_keys`

```
sed -i 's/#PasswordAuthentication yes/PasswordAuthentication no/g' /etc/ssh/sshd_config
sed -i 's/#Port 22/Port 2222/g' /etc/ssh/sshd_config
```

## `scp`
```
scp .ssh/id_ed25519.pub pve:/root/.ssh
```

- [[SSH Port Forwarding]]
