## Open source documentation with Couscous

Attempted on a mid-2014 Macbook Pro running OSX Yosemite.


## Installation

	curl -OS http://couscous.io/couscous.phar

This failed for me and so I had to download the file through my browser
Change permissions for Couscous and move to root path

	chmod +x couscous.phar
	sudo mv couscous.phar /usr/local/bin/couscous

This failed because I needed to edit my `php.ini` file.

	php -i | grep "php.ini"

found the file in `/etc/`. I added to it the line
	
	date.timezone = "America/Los_Angeles"

## Running couscous

Navigate to local copy of a GitHub repo containing `.md` files and run the following command:

	couscous preview

And then visit a version of the site running at [http://localhost:8000/](http://localhost:8000/)
If you edit any of the underlying `.md` files, the preview version updates automatically (just refresh the page in your browser)

## Using Couscous

Test the site appearance

	couscous preview

Any file named `README.md` gets converted to `index.html`. Sub-pages of the documentation are any other `.md` files in the directory, they can be found at [http://localhost:8000/myproject/otherMDfile.html](http://localhost:8000/myproject/otherMDfile.html)

Make sure that the directory holding the `.couscous` file is a functional GitHub repository. For a project with a single algorithm in multiple languages, I made a separate repository for documentaion. Now run

	couscous deploy

which sends the site to [http://your-username.github.io/your-project/](http://your-username.github.io/your-project/.)

Now customize using a `couscous.yml` file in root directory

## Change URL if hosting through Google Sites

Register the GitHub domain as a redirect from your purchased Google Sites URL
For specific subpages that you want to have a special link, for now the best option is to individually redirect a subdomain.

	flowtrace.org ---> http://www.williamgilpin.github.io/flowtrace_docs/
	gallery.flowtrace.org ---> http://www.williamgilpin.github.io/flowtrace_docs/gallery

