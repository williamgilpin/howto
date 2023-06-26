### Link your local to GitHub account via SSH

GitHub no longer supports password authentication. Instead, you can use SSH keys or a personal access token (PAT). I prefer SSH keys, because they are a bit more general and can be used for other things.

In terminal,
    
    ssh-keygen -o -t rsa -C "username@email.com"

Press enter twice to assign to default location and have no password. Now view the SSH key by going to

    cat /n/home03/wgilpin/.ssh/id_rsa.pub

Copy and paste this into your SSH key collection on the GitHub website. To test that this is set up correction, on your local machine run

    ssh -T git@github.com

and receive response

    Hi username! You've successfully authenticated, but Github does
    not provide shell access.

A nice guide is [here](https://kbroman.org/github_tutorial/pages/first_time.html)


### fork repo online

clone forked repo locally

      >> git clone "https://...MY_USERNAME...

add upstream branch

    >> git remote add upstream "https://...THEIR_USERNAME...git

make a new branch

     >> git add branch BRANCH_NAME

switch to new branch and make edits

       >> git checkout BRANCH_NAME

push new commits

     >> git add.
     >> git commit -m "test commit plz ignore"
     >> git push

go to github and make a pull request



### Editing commit history

To alter or combine the last four commits, run
```
   $ git rebase -i HEAD~4
```
A text editor will pop up. Replace "pick" with "squash" for the commits that you want to merge together. It will then prompt you to come up with a new commit message for all of the commits that you just squashed.

Save and close using standard emacs commands

If you've already commited, you have to force the update:
  
  $  git push origin master --force

### Remove a "dirty" commit containg a large or private file

If you commit a large file that is rejected on push (for example, GitHub will reject files >100MB), you need to completely remove it from the commit history before you will be able to push again. This is a also good idea if you have committed private file that you don't want to be public.

Install bfg

    brew install bfg

Remove the file from the history. Don't specify the path, just the filename (e.g. `my_bad_file.zip`)

    bfg --delete-files my_bad_file.zip

Fix the commit history to remove this bad file

    git reflog expire --expire=now --all && git gc --prune=now --aggressive

If using `bfg` fails, try overrwriting the hashes. This can cause issues on shared repositories, and should be used as a last resort.

    git filter-branch --force --index-filter "git rm --cached --ignore-unmatch <path/filename>" --prune-empty --tag-name-filter cat -- --all
    git push origin master --force


### Examine and merge a pull request

After recieving a pull request, make sure your local copy of the repository is up to date with `master` and that you've committed all changes. Now,

	git checkout -b otherusersname-master master
	git pull https://github.com/otherusersname/pypdb.git master

Now run tests, make sure everything appears to be working. You can also make any edits to the documentation, etc on this branch. Once you are satisfied (and if there are no conflicts), merge this branch:

	git checkout master
	git merge --no-ff otherusersname-master
	git push origin master

If you get an error when switching branches, you might need to discard some local changes to master (do this carefully). In this case, use the force flag
  
  git checkout -f master


### Fork a repository

Detailed instructions [here](https://help.github.com/articles/fork-a-repo/)

You can fork a repository and make basic changes from the online GitHub GUI. After forking and making any changes online, you can get a local copy by running

  git clone https://github.com/username/repo_name

### Update local with changes to remote

  git pull origin

This combines a `fetch` with a `merge`

### Force overwrite local with remote

	git fetch origin
	git reset --hard origin/master



# Errors

### Cannot stage changes

Sometimes instead of `git add .` you need to use `git add --all`
This can be fixed by stashing and then immediately un-stashing:

    git stash
    git stash apply


## Permission issues

`error: insufficient permission for adding an object to repository database .git/objects`

Somehow the ownership got messed up for some files. From project base directory, try running

    cd .git/objects
    ls -al
    sudo chown -R yourname:yourgroup *

yourname and yourgroup can be figured out by seeing what the majority of of the ls -al usernames and groups are. My "group" appeared to be staff for some reason. This answer is taken from [StackExchange](http://stackoverflow.com/questions/6448242/git-push-error-insufficient-permission-for-adding-an-object-to-repository-datab)


## Recieve warnings about passwords being deprecated 

After using GitHub from the command line, I recieved the following email


    Hi @williamgilpin,

    You recently used a password to access the repository at williamgilpin/dysts with git using git/2.24.3 (Apple Git-128).

    Basic authentication using a password to Git is deprecated and will soon no longer work. Visit https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information around suggested workarounds and removal dates.

    Thanks,
    The GitHub Team


I follwed GitHub's instructions [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) to create a PAT. 

To store the PAT after creating it, I follwed the instructions 
+ [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)
+ and then [here](https://docs.github.com/en/get-started/getting-started-with-git/updating-credentials-from-the-macos-keychain)
+ I also removed the file `~/..git-credentials`
+ Other useful information about storing PAT [here](https://askubuntu.com/questions/773455/what-is-the-correct-way-to-use-git-with-gnome-keyring-and-https-repos/959662#959662) and [here](https://stackoverflow.com/questions/46645843/where-to-store-the-personal-access-token-from-github)

### Transfer repo to an organization

Transfer as normal using the "Settings tab"

### Global Configurations

My `~/.gitconfig` file is as follows

    [user]
            name = myname
            email = myemail@email.com
    [core]
            editor = emacs
    [credential]
            helper = store
    [alias]
            acp = !git add . && git commit -m "latest" && git push

### Removing git-lfs

Oftentimes, you might find yourself needing to completely remove git-lfs from a respository, and then re-add the files it tracks to git. Remove all traces of git-lfs from `.gitattributes`. Then, from the command line, run

    git lfs uninstall

You will likely still need to manually go through and untrack every file that was previously tracked by git-lfs. This can be done by running

    git lfs untrack filename

You can list out all tracked files by running

    git lfs ls-files
  

## Deprecated: connecting a new computer to GitHub using password authentication

(Old) To use traditional authentication, in Terminal,

    git config --global user.name github_username
    git config --global user.email my_email@email.com
    git config --global core.editor emacs

The last line sets the default editor to emacs. The first time you push changes to remote, you will be prompted for your password. This will be saved for future use

If you are still repeatedly prompted for your account credentials, use

    git config credential.helper store

Note that running the above will cause an unhashed copy of your GitHub password to be stored locally.


