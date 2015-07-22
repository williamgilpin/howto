fork repo online

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



# Editing commit history

To alter or combine the last four commits, run

   $ git rebase -i HEAD~4

A text editor will pop up. Replace "pick" with "squash" for the commits that you want to merge together. It will then prompt you to come up with a new commit message for all of the commits that you just squashed.

If you've already commited, you have to force the update:
  
  $  git push origin master --force
