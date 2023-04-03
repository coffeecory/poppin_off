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

---

FIX Pictures not uploading to GitHub

First go to 

Setting > file and links > new link format > set to relative path

then disable wikilinks format

Then install plugin, "Upgrade Relative Links"

Turn the plugin on.

Press,  Ctrl+P > Type links, > Select, upgrade relative links

You may need to delete the \[  bracket  prepended at the start of the link there is a duplicate that doesn't need to be there !\[[

https://forum.obsidian.md/t/include-images-when-pushing-to-github/14315

https://docs.github.com/en/enterprise-server@3.4/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes#relative-links-and-image-paths-in-readme-files

https://www.youtube.com/watch?v=R6euByfGaN4

https://docs.github.com/en/repositories/managing-your-repositorys-settings-and-features/customizing-your-repository/about-readmes

https://forum.obsidian.md/t/obsidian-has-trouble-creating-new-notes-from-relative-path-to-file-links/3741

For #2, most programs still do not support and recognize wiki style links, which is what [[link]] is.  Markdown links, which is what [link](relative/path/to/link.md) is industry standard and is portable. Obsidian should be tracking and updating links appropriately, but that is a failure in obsidian itself. There are two plugins since that can help keep up on the automatic renaming: consistent attachments and links, and one called update relative links


Upgrade Relative Links README
## Plugin restrictions

The `Use [[Wikilinks]]` option must be turned off to use Markdown's link syntax. The point of using relative paths is also to make notes more generic, and if you are also using Wiki Links, there is no need to use relative paths.

---



