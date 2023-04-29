# NAT Traversal
First, the protocol should be based on [[UDP]]. You _can_ do NAT traversal with [[TCP]], but it adds another layer of complexity to an already quite complex problem, and may even require [[Linux Kernel|kernel]] customizations depending on how deep you want to go. We’re going to focus on UDP for the rest of this article.

## Links
- [How NAT traversal works · Tailscale](https://tailscale.com/blog/how-nat-traversal-works/)
- [[Tailscale]]