
.. toctree::
   :hidden:
   :maxdepth: 2
   :caption: Contents:

   what
   basic


Basics
=============
1. create/clone repository
2. recording changes: add, commit
3. check status
4. ignore files
5. moving files
6. view history
7. undoing things
	a. git commit --amend
	b. unstage staged file
	c. unmodify modified file
8. remotes
	a. show the remotes, git remote -v
	b. add remote repositories
	c. fetch and pull from remotes
	d. push to remotes, git push <remote> <branch>
	e. inspecting remote
	f. rename and remove remotes
	g. tagging:
		i. list tags
		ii. create tag
		iii. sharing tags
		iv. sharing tags
		v. delete tags
		vi. checkout tags

Git branching
=============
1. internal structure:
	a. trees, blobs and commits
2. branch is a lightweight movable pointer
3. master and HEAD
4. create a new branch
5. switching branches
6. basic branching
7. basic merging
8. basic marge conflicts
9. branch management
10. branching workflows
11. remote branches:
	a. git fetch - update remote tracking branch - synchronize with given remote
		i. when fetching new remote-tracking branch:
			merge it into some branch (git merge origin/some-branch or
            create a new local branch for it (git checkout -b some-branch origin/sone-branch
	b. git push - sharing local changes with the world
	c. tracking branches - git branch -vv
	d. pulling
		i. git pull =~ git fetch + git merge. the later is preffered
	e. delete remote branch
		i. git push origin --delete some-branch
	f. rebase
		i. simple rebase
		ii. rebase --onto
		iii. Do not rebase commits that exist outside your repository and people may have based work on them


.. [1] https://en.wikipedia.org/wiki/SHA-1
