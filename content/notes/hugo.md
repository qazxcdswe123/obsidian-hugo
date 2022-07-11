```bash
# Add front-matter to every file that dont have front-matter
for f in *.md; do
topLine=$(sed -n 1p $f)
if [ "$topLine" != "---" ]; then
new=$(echo $f | cut -d '.' -f 1) ;sed -i "1s/^/---\ntitle: $new\n---\n/" $f
fi
done
```

```bash
# check for no front-matter
for f in *.md; do
topLine=$(sed -n 1p $f)
if [ "$topLine" != "---" ]; then
echo "$f has no dash"
fi
done
```