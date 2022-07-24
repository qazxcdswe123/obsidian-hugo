---
aliases: 
tags: 
date: Jul 24th, 2022
---

```bash
#!/bin/bash

for f in *.md;
do
  topLine=$(sed -n 1p "$f")
  new=$(echo "$f" | cut -d '.' -f 1)
  if [ "$topLine" != "---" ]
  then
    sed -i "1s/^/---\ntitle: $new\n---\n/" "$f"
  else
    sed -i "2s/^/title: $new\n/" "$f"
  fi
done
```