# How to Sync Obsidian to GitHub

## Create Repo on GitHub
Use VSCode to clone repo locally on C users drive location
Install Obsidian
Install Plugin obsidian git and enable it.
Create README file obsidian will auto prepend .md
Go back to VSCode or run the following commands in your terminal:

	git config --global user.email "you@example.com"
	git config --global user.name "Your Name"

Then create the .gitignore file first commiting it up to github before the rest of your files so that it tells github to not allow pushing of whatever files you specifiy in the .gitignore file. Commands for this are as so:

	git add ./gitignore
	git commit -m "Commiting gitignore before anything else." ./gitignore
	git checkout
	git push origin master <or main> <or other remote branch you created>

Then from there move back to VSCode and commit all the remainding files you to the remote repo. 

Move back to Obsidian modify the README to say:

	Obsidian master
