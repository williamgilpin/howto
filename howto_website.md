Making a website using GitHub pages

## Overview

Previously, the easiest options have been either to either:
+ Directly edit an HTML file and then use GitHub Pages
+ Make a website in Markdown and render it using Couscous, a PHP-based Markdown to HTML converter

However, as of December 2016 GitHub will by default render Markdown using Jekyll when this feature is enabled in a GitHub repository ([instructions here](https://github.com/blog/2289-publishing-with-github-pages-now-as-easy-as-1-2-3)). You can specify the branch in the online repo settings; for documentation-only repos, it is probably easiest to just use the master branch.

## Changing the theme

If you change the Markdown theme using the GitHub web editor, you will need to synchronize your local copy with the theme template used in the remote. The safest way to do this is:
+ Push all your content changes to the remote branch
+ Edit the Jekyll theme/other web settings
+ In your local branch run

	$ git pull

However, the best way to change formatting is to pick specify the Jekyll theme/other attributes with a local _config.yml file. This also allows you a little more control over your choice of theme. I particularly like the "minima" theme, which can be accessed by adding to your `_config.yml` this line:

	theme: minima

## Further customization

The default themes have various options that can be partly edited by changing the frontmatter of individual Markdown files (or all the defaults in the `_config.yml` file)

[How to specify front matter in single files](https://jekyllrb.com/docs/frontmatter/)
[A list of page layout styles for a single theme, Minima](https://github.com/jekyll/minima/tree/master/_layouts)
[Setting defaults for front matter using config file](https://jekyllrb.com/docs/configuration/#front-matter-defaults)

[More info about configuring Jekyll on GitHub Pages](https://help.github.com/articles/configuring-jekyll/)

## Change URL if hosting through Google Sites

Register the GitHub domain as a redirect from your purchased Google Sites URL
For specific subpages that you want to have a special link, for now the best option is to individually redirect a subdomain.

	flowtrace.org ---> http://www.williamgilpin.github.io/flowtrace_docs/
	gallery.flowtrace.org ---> http://www.williamgilpin.github.io/flowtrace_docs/gallery

## Notes and Miscellaneous

After trying to customize, the page will not render, and checking the repo settings reveals a build error message "The value 'nil' was passed to a date-related filter that expects valid dates..."
+ If you override the Jekyll defaults for GitHub pages, you need to at least specify a dummy date in your config defaults file
	
On Chrome, you can bypass the cached version of the page using Command + Shift + R. This is useful for previewing updates.

Be very, very careful when using a .gitignore. I tried to set mine to ignore all tilde (~) files created by my text editor, and the page formatting repeatedly failed.

Don't mess around with baseURL in your `_config.yml` file. This may cause the Jekyll theme not to render properly (see [this GitHub issue thread](https://github.com/spf13/hugo/issues/1421))

I added a Google Analytics script using HTML, but it's also possible to specify it as an attribute in the Markdown file. (see [this StackExchange thread](http://stackoverflow.com/questions/17207458/how-to-add-google-analytics-tracking-id-to-github-pages))

