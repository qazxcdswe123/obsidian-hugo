
## Diff
- Compare with previous commit: use `^!`
	- `git diff 77e13ax^!`
- Compare specific directory
	- `git diff hash1 hash2 - path/to`
- See the number of changes
	- `git diff —stat hash1 hash2`
- See what in staged area
	- `git diff —staged`

- `hash-object` converts an existing file into a git object
- `cat-file` prints an existing git object to the standard output.

## Config
[Telling Git about your signing key - GitHub Docs](https://docs.github.com/en/authentication/managing-commit-signature-verification/telling-git-about-your-signing-key)  
[Generating a new SSH key and adding it to the ssh-agent - GitHub Docs](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent)

```bash
git config --global gpg.format ssh
pbcopy < ~/.ssh/id_ed25519.pub
git config --global user.signingkey 'key'
git config --global commit.gpgsign true
git config --global tag.gpgsign true
git config --global color.ui auto
```

To get particular config value, use `--get`  
`git config --get --global color.ui`

To get all config value, use `--list`  
`git config --list`  
or look at your `~/.gitconfig` file. The local configuration will be in your repository's `.git/config` file.  
`git config --list --show-origin`
