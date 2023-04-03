---
aliases: []
date created: Mar 31st, 2023
date modified: Mar 31st, 2023
---

## [[PVE]]

```
curl -fsSL https://tailscale.com/install.sh | sh

bash -c "$(wget -qLO - https://github.com/tteck/Proxmox/raw/main/misc/add-tailscale-lxc.sh
tailscale up --advertise-routes=192.168.0.0/16
```
1. Install tailscale in an lxc container and set to `Start at boot` (`bash -c "$(wget -qLO - https://github.com/tteck/Proxmox/raw/main/misc/add-tailscale-lxc.sh)" -s 106
`)
2. In the lxc container, set `tailscale up --advertise-routes=192.168.0.0/16`, and review it in the admin console.
3. In the client side (Your local machine, `MacOS` for example), set `sudo tailscale up --accept-routes`
