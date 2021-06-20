### Link to GitHub account

Using SSH

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

   $ git rebase -i HEAD~4

A text editor will pop up. Replace "pick" with "squash" for the commits that you want to merge together. It will then prompt you to come up with a new commit message for all of the commits that you just squashed.

Save and close using standard emacs commands

If you've already commited, you have to force the update:
  
  $  git push origin master --force


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


## Deprecated: connecting a new computer to GitHub using password authentication

(Old) To use traditional authentication, in Terminal,

    git config --global user.name github_username
    git config --global user.email my_email@email.com
    git config --global core.editor emacs

The last line sets the default editor to emacs. The first time you push changes to remote, you will be prompted for your password. This will be saved for future use

If you are still repeatedly prompted for your account credentials, use

    git config credential.helper store

Note that running the above will cause an unhashed copy of your GitHub password to be stored locally.

