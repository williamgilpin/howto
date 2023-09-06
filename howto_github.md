
Getting Started with: Git, GitHub, and GitHub pages
==============

## Setting up git and GitHub for the first time {#first}

1. Install git on your local computer by following the instructions [here](https://git-scm.com/book/en/v2/Getting-Started-Installing-Git). Git is a code project management tool that is used primarily for version control and collaboration. The [documentation](https://git-scm.com/doc) is excellent.

2. Make a GitHub account. You might consider applying to link your account to your school email via [GitHub for Education](https://education.github.com/). This comes with a lot of perks, like private repositories and free access to the [GitHub Copilot](https://github.com/features/copilot) plugin for VSCode and PyCharm.

3. Create a local project folder on your computer containing code that you want to track. For example, you might want to create a folder for your course homeworks, or for labs, or for the final project. For now, let’s just make a test repository, to make sure that everything is working.

```bash
$ mkdir test_repo
$ cd test_repo
```

4. You should now be inside your new repository. Add a README.md file to your local repository. You can use a text editor like VSCode, Jupyter Lab, or Sublime Text, or you can do this in the Terminal with your preferred editor. On macOS I normally use emacs ([information here](https://wikemacs.org/wiki/Installing_Emacs_on_OS_X)), but many may prefer nano or vim. If you want to use a different editor, replace emacs in all of the following steps with your preferred editor.

```
$ emacs README.md
```

5. If this is your first time setting up GitHub and git, create a top-level file on your system called `.gitconfig`. Mine is located at the top level `~/.gitconfig` and contains the following lines

```bash
[user]
        name = williamgilpin
        email = williamgilpin@gmail.com
[core]
        editor = emacs
[credential]
        helper = store
```

Of these lines, the `[user]` and `[credential]` fields are the most important fields. 

6. We now want to create the online repo, which is known as the `remote` repository. In your web browser, log into your GitHub account, and then make a repository with the exact same name as your local project folder. When prompted, do *not* initialize your online remote repo with a README or license. When the empty repository has been created, it should be located online.

	https://github.com/yourusername/test_repo

7. If this is your first time using GitHub, you need to create Personal Access Token (PAT), which GitHub uses instead of passwords when you access a remote repo from th Terminal. Go to the GitHub website and make sure that you are logged in. As of writing, the web interface to create a PAT is as follows:

+ Go to github.com
+ Select your profile on the right side and go to: Settings > Developer Settings (bottom of left sidebar)
> Personal Access Tokens > Tokens (classic) > Generate New Token (classic)
+ You will encounter a screen where you name your token and then set granular permissions for the token. I chose to use a Classic token with no expiration, and I enabled full permissions for everything on the Token.
+ Hit “Generate Token” when you are ready.
+ You will be taken to a landing page with a list of your tokens. Copy the one you just created, which is likely a long string of letters and numbers. This will likely be the only token on this list.

If you run into difficulty, please follow the more detailed instructions provided by GitHub on created a PAT [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token).
If setting up a PAT fails, then you might instead opt to authenticate with SSH. See the instructions[here](#ssh)

8. Now return to your empty repo's GitHub page, https://github.com/yourusername/test_repo. There will be instructions there listing what to do in order to get everything working on your local repo, but I've summarized them here. In your Terminal, navigate to your local repo. You will run the following commands in sequence:

```bash
$ git init
$ git add .
$ git commit -m "first commit"
$ git branch -M main
$ git remote add origin https://github.com/yourusername/test_repo.git
$ git push -u origin main
```

These commands first tell git to treat the directory as a `git` project with version tracking. The `git add .` command then adds all files or file changes. The branch command then confirms that you are on the primary project branch, and the `git remote` command actually initiates the connection to the remote repository you just made online with GitHub.

The final `git push` command sends your local changes to the remote repository. For your first push, GitHub will prompt you to provide a username, followed by a password. *Instead of your GitHub.com password, please enter the PAT that you created in the last step*.


If everything works, your Terminal will show a message like the following

```bash
(base) william@cns-f-pmaa59131 test_repo % git push
Enumerating objects: 7, done.
Counting objects: 100% (7/7), done.
Delta compression using up to 10 threads
Compressing objects: 100% (4/4), done.
Writing objects: 100% (4/4), 60.62 KiB | 2.53 MiB/s, done.
Total 4 (delta 3), reused 0 (delta 0), pack-reused 0
remote: Resolving deltas: 100% (3/3), completed with 3 local objects.
To https://github.com/williamgilpin/test_repo
   e049541..ee2cb7d  main -> main
```

9. Now that git is working, you can modify and update your local repository, and then manually push updates to your remote. To practice these steps, make some changes to your local repository; for example, by editing into your `README.md` file. 

```bash
$ emacs README.md
```
Whenever you want to apply those changes to the remote (the GitHub version of your code), first add these files in the Terminal (make sure you are in your repository). Since we already made a `README.md` file, you will need to start by staging the changes in your local repository. 

```bash
$ git add .
```

10. Then commit the changes with a short but descriptive message

```bash
$ git commit -m "added example changes to the README file"
```

11. Then finally send the update to GitHub

```bash
$ git push
```

Both your local and the GitHub versions of your repo will keep track of the sequence of commits you've applied, making it easier to roll back your changes at any time. You'll notice that GitHub treats `README.md` as a special file---it renders it into a nice page, similar to a website's index page, that represents the first thing a user sees when they look at your repo. Usually we want to put a description of the repo, dependencies, and a minimal working example into the README.md---although sometimes the README contains full documentation, graphics, etc. The Google [Jax repository](https://github.com/google/jax) is a great example. Rather than HTML, the markup language used for README files is Markdown, which is like a blend of HTML and LaTeX with lighter syntax than either one. You can learn more from the [Markdown guide](https://www.markdownguide.org/basic-syntax/) or by looking at [the unrendered version](https://raw.githubusercontent.com/williamgilpin/cphy/main/README.md) of this course's own README file

You might have local files that you don't want to appear in your public repo. For example, in the course repository I have solution files, as well as personal files like cached data, that I don't want to appear on GitHub. For files of this nature, it's usually a good idea to create a file called `.gitignore` in the top-level repository of your local repo. This specifies files or patterns that should be ignored. See the [gitignore documentation](https://git-scm.com/docs/gitignore) as well as [the one I'm using for the course repo](https://github.com/williamgilpin/cphy/blob/main/.gitignore)

## Create a website using GitHub pages

We are now going to a create a basic website to accompany our repository. This isn’t always necessary, but this feature is useful to quickly create a website—--for example, for [the computational physics course webpage](https://www.wgilpin.com/cphy/) is written entirely in Markdown, and rendered into HTML automatically every time an update is pushed to GitHub (which also provides free hosting for small websites)

1. The best approach is to follow the instructions [from GitHub](https://pages.github.com/). Use the instructions for a Project Site. 

+ Create a new git and GitHub repository, or go to an existing repository's settings in the online GitHub GUI 
+ In the Settings menu, go to "Pages" in the sidebar. Enable GitHub pages and, if prompted, pick a source as your `main` or `master` branch. 

After some time passes, Github will automatically convert your `README.md`` file into an index.html file and then host it at:

	https://yoursusername.github.io/my_repository

GitHub pages are structured as “actions” that run every time you push from your local to the remote on GitHub. This is similar to automated testing, which we will explore in a future lab. As a result, your website won’t automatically update as quickly as the repo itself, due to an extra “build” step. If the “build” fails, then on your repository you will see a red “X” on the commit. An orange dot indicates that the build has not occurred yet. If your website has still not updated, go to the URL and refresh the page with a clear cache; [CMD] + [Shift] + R

## Collaboration

When used for single projects, GitHub acts sort of like a manual Dropbox folder, where you deliberately decide when to update the copy of your code that exists in the cloud. This might seem tedious, but as projects grow it becomes useful to keep track of versions, run automated tests before commits, check for conflicting commits, etc. One of the most important use cases is collaboration, where multiple people are working with the same remote repository.

+ Fork the repository on GitHub [via these instructions](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository)
+ Make any changes that you want. It's probably best to start with something small, like fixing small errors
+ Make sure that your local branch is up-to-date with the course using fetch (see instructions [here](https://stackoverflow.com/questions/7244321/how-do-i-update-or-sync-a-forked-repository-on-github)). This is to account for the case where I've made changes to the course repo while you've been making your changes.
+ When everything looks good, submit a pull request [using the instructions here](https://docs.github.com/en/pull-requests/collaborating-with-pull-requests/proposing-changes-to-your-work-with-pull-requests/creating-a-pull-request)

For smaller projects (like class projects), it isn't necessary to use pull requests---instead, you can [invite collaborators to a shared repository](https://docs.github.com/en/account-and-profile/setting-up-and-managing-your-personal-account-on-github/managing-access-to-your-personal-repositories/inviting-collaborators-to-a-personal-repository), and everyone will be able to make commits.

Important: if you have a fork that you are updating from a main---such as a fork of a class repository that you are using to complete homeworks--make sure that you don’t use your assignment fork to submit pull requests to my main repository. Since your versions of the assignments will override mine, it could lead to weird merge conflicts. If you fork a single version of an active repo (like a class repo), periodically [`git pull`](https://git-scm.com/docs/git-pull) to get any changes. Just double check to make sure that to `git stash` any changes you've made locally (like assignments)

### Link your local machine to GitHub account via SSH {#ssh}

GitHub no longer supports password authentication. Instead, you can use SSH keys or a personal access token (PAT). I prefer SSH keys, because they are a bit more general and can be used for other things.

In terminal,
    
```bash
    ssh-keygen -o -t rsa -C "username@email.com"
```

Press enter twice to assign to default location and have no password. Now view the SSH key by going to

```bash
    cat ~/.ssh/id_rsa.pub
```

Copy and paste this into your SSH key collection on the GitHub website. To test that this is set up correction, on your local machine run

```bash
    ssh -T git@github.com
```

and receive response

```bash
    Hi username! You've successfully authenticated, but Github does
    not provide shell access.
```

A nice guide is [here](https://kbroman.org/github_tutorial/pages/first_time.html)


### Fork a repo online and then submit a pull request {pull-request}

1. Create a local clone of the target repository

    git clone http://github.com/williamgilpin/repo_name

If you are repeatedly prompted to authenticate, but run into issues because GitHub no longer accepts passwords, you can use the git protocol instead of https. This requires that you have an SSH key set up (see above). To do this, run

    git clone git@github.com:williamgilpin/repo_name.git

If this still fails, then check that you have SSH set up correctly. See the instructions[here](#ssh)

2. Now fork the repository to your own GitHub account. Go to the original repository on the GitHub web interface and click the "Fork" button.

3. Add your fork as a remote:

```bash
    git remote add myfork https://github.com/YOUR_USERNAME/repo_name.git
```

4. Create a new branch to work on:

```bash
    git checkout -b newfeature
```

5. Make your changes, and commit them:

```bash
    git add .
    git commit -m "Added newfeature"
```
    
6. Push your changes to your fork:

```bash
    git push myfork newfeature
```

7. On the GitHub web interact, create a pull request from your `newfeature`` branch to the original repo's main branch.

8. If the original maintainer requests changes, or you make further changes, commit them to your `newfeature`` branch. Then push to your fork again. The PR will automatically update.

9. Once approved and merged, you can delete your local branch and pull the updated main branch:

```bash
    git branch -d newfeature
    git checkout main
    git pull origin main
```

### Create a new feature

On your local copy of the repo, make sure that you are updated to the latest version of the remote

```bash
    git pull
```

Now create a new branch locally

```bash
    git checkout -b [name_of_your_new_branch]
```

Now push to the remote

```bash
    git push origin [name_of_your_new_branch]
```

Now make edits to your local version, pushing to the remote as needed. Occasionally, you may also need to pull the latest changes from the remote main.

### Editing commit history

To alter or combine the last four commits, run

```bash
   $ git rebase -i HEAD~4
```
A text editor will pop up. Replace "pick" with "squash" for the commits that you want to merge together. It will then prompt you to come up with a new commit message for all of the commits that you just squashed.

Save and close using standard emacs commands

If you've already commited, you have to force the update:

```bash
  $  git push origin master --force
```

### Remove a "dirty" commit containg a large or private file

If you commit a large file that is rejected on push (for example, GitHub will reject files >100MB), you need to completely remove it from the commit history before you will be able to push again. This is a also good idea if you have committed private file that you don't want to be public.

Install bfg

```bash
    brew install bfg
```

Remove the file from the history. Don't specify the path, just the filename (e.g. `my_bad_file.zip`)

```bash
    bfg --delete-files my_bad_file.zip
```

Fix the commit history to remove this bad file

```bash
    git reflog expire --expire=now --all && git gc --prune=now --aggressive
```

If using `bfg` fails, try overrwriting the hashes. This can cause issues on shared repositories, and should be used as a last resort.

```bash
    git filter-branch --force --index-filter "git rm --cached --ignore-unmatch <path/filename>" --prune-empty --tag-name-filter cat -- --all
    git push origin master --force
```

### Examine and merge a pull request

After recieving a pull request, make sure your local copy of the repository is up to date with `master` and that you've committed all changes. Now,

```bash
	git checkout -b otherusersname-master master
	git pull https://github.com/otherusersname/pypdb.git master
```

Now run tests, make sure everything appears to be working. You can also make any edits to the documentation, etc on this branch. Once you are satisfied (and if there are no conflicts), merge this branch:

```bash
	git checkout master
	git merge --no-ff otherusersname-master
	git push origin master
```

If you get an error when switching branches, you might need to discard some local changes to master (do this carefully). In this case, use the force flag
  
```bash
    git checkout -f master
```

### Fork a repository online

You can fork a repository and make basic changes from the online GitHub GUI. After forking and making any changes online, you can get a local copy by running

    git clone https://github.com/username/repo_name

Detailed instructions [here](https://help.github.com/articles/fork-a-repo/)

### Update local with changes to remote

```bash
    git pull origin
```

This combines a `fetch` with a `merge`. If you want to do these separately, you can run

```bash
    git fetch origin
    git merge origin/master
```

If you have uncommitted changes, you may need to stash them before pulling

```bash
    git stash
    git pull origin
```

You can then add your changes back

```bash
    git stash pop
```

### Force overwrite local with remote

```bash
	git fetch origin
	git reset --hard origin/master
```

### Downloading a remote repository without forking it

Sometimes you just want to download a copy of someone's code without collaborating, forking, etc. For situations like these, you can use [git clone](https://docs.github.com/en/repositories/creating-and-managing-repositories/cloning-a-repository). I recommend cloning from the HTTP address rather than the git// address of the repo

### Installing a Python Package from GitHub

If there's a setup.py file in the repo, you can install using pip

pip install git+git://github.com/someusername/somerepo

### Modifying commit history

To alter or combine the last four commits, run

```bash
$ git rebase -i HEAD~4
```

A text editor will pop up. Replace "pick" with "squash" for the commits that you want to merge together. It will then prompt you to come up with a new commit message for all of the commits that you just squashed.

If you've already commited, you have to force the update:

```bash
$ git push origin main --force
```

### Forking a repository summarized

clone forked repo locally

```bash
$ git clone "https://...MY_USERNAME...
```
add upstream branch

```bash
$ git remote add upstream "https://...THEIR_USERNAME...git
```
make a new branch
```bash
$ git add branch BRANCH_NAME
```
switch to new branch and make edits
```bash
$ git checkout BRANCH_NAME
```
push new commits
```bash
$ git add .
$ git commit -m "test commit plz ignore"
$ git push
```
go to github and make a pull request



# Errors

### Cannot stage changes

Sometimes instead of `git add .` you need to use `git add --all`
This can be fixed by stashing and then immediately un-stashing:

```bash
    git stash
    git stash apply
```

## Permission issues

`error: insufficient permission for adding an object to repository database .git/objects`

Somehow the ownership got messed up for some files. From project base directory, try running

```bash
    cd .git/objects
    ls -al
    sudo chown -R yourname:yourgroup *
```

yourname and yourgroup can be figured out by seeing what the majority of of the ls -al usernames and groups are. My "group" appeared to be staff for some reason. This answer is taken from [StackExchange](http://stackoverflow.com/questions/6448242/git-push-error-insufficient-permission-for-adding-an-object-to-repository-datab)


## Recieve warnings about passwords being deprecated 

After using GitHub from the command line, I recieved the following email

```bash
    Hi @williamgilpin,

    You recently used a password to access the repository at williamgilpin/dysts with git using git/2.24.3 (Apple Git-128).

    Basic authentication using a password to Git is deprecated and will soon no longer work. Visit https://github.blog/2020-12-15-token-authentication-requirements-for-git-operations/ for more information around suggested workarounds and removal dates.

    Thanks,
    The GitHub Team
```

I followed GitHub's instructions [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token) to create a PAT. 

To store the PAT after creating it, I follwed the instructions 
+ [here](https://docs.github.com/en/github/authenticating-to-github/keeping-your-account-and-data-secure/creating-a-personal-access-token)
+ and then [here](https://docs.github.com/en/get-started/getting-started-with-git/updating-credentials-from-the-macos-keychain)
+ I also removed the file `~/..git-credentials`
+ Other useful information about storing PAT [here](https://askubuntu.com/questions/773455/what-is-the-correct-way-to-use-git-with-gnome-keyring-and-https-repos/959662#959662) and [here](https://stackoverflow.com/questions/46645843/where-to-store-the-personal-access-token-from-github)




### Transfer repo to an organization

Transfer as normal using the "Settings tab"

### Global Configurations

My `~/.gitconfig` file is as follows

```bash
    [user]
            name = myname
            email = myemail@email.com
    [core]
            editor = emacs
    [credential]
            helper = store
    [alias]
            acp = !git add . && git commit -m "latest" && git push
```

### Removing git-lfs

Oftentimes, you might find yourself needing to completely remove git-lfs from a respository, and then re-add the files it tracks to git. Remove all traces of git-lfs from `.gitattributes`. Then, from the command line, run

    git lfs uninstall

You will likely still need to manually go through and untrack every file that was previously tracked by git-lfs. This can be done by running

    git lfs untrack filename

You can list out all tracked files by running

    git lfs ls-files
  

## Deprecated: connecting a new computer to GitHub using password authentication

These instructions no longer work, now that GitHub dropped support for password authentication.

To use traditional authentication, in Terminal,

    git config --global user.name github_username
    git config --global user.email my_email@email.com
    git config --global core.editor emacs

The last line sets the default editor to emacs. The first time you push changes to remote, you will be prompted for your password. This will be saved for future use

If you are still repeatedly prompted for your account credentials, use

    git config credential.helper store

Note that running the above will cause an unhashed copy of your GitHub password to be stored locally.

## I receive the following "error: unable to read askpass response from '/usr/libexec/openssh/gnome-ssh-askpass'"

Run the following command to fix this issue

    unset SSH_ASKPASS


