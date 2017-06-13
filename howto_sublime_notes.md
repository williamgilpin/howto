

### Enable automatic browser refreshing on build using an extension

Instructions taken from [the documentation](http://gcollazo.github.io/BrowserRefresh-Sublime/)

Navigate to the packages directory of Sublime Text

	cd /Applications/Sublime\ Text.app/Contents/MacOS/Packages/

In this directory, install the package

	git clone https://github.com/gcollazo/BrowserRefresh-Sublime.git "Browser Refresh"

Now in Sublime Text go to Preferences > Key Bindings and add

	[
	    {
	        "keys": ["command+shift+r"], "command": "browser_refresh", "args": {
	            "auto_save": true,
	            "delay": 0.5,
	            "activate": true,
	            "browsers" : ["chrome"]
	        }
	    }
	]

Now if you open the HTML version of your document in a Chrome tab, running the keyboard shortcut will autosave and refresh the tab. You can now couple this to another extension that builds a Markdown file on autosave, or you can edit HTML files directly in Sublime Text


### Rendering LaTeX equations with MathJax

At the end of your Markdown document, add this snippet

	<style TYPE="text/css">
	code.has-jax {font: inherit; font-size: 100%; background: inherit; border: inherit;}
	</style>
	<script type="text/x-mathjax-config">
	MathJax.Hub.Config({
	    tex2jax: {
	        inlineMath: [['$','$'], ['\\(','\\)']],
	        skipTags: ['script', 'noscript', 'style', 'textarea', 'pre'] // removed 'code' entry
	    }
	});
	MathJax.Hub.Queue(function() {
	    var all = MathJax.Hub.getAllJax(), i;
	    for(i = 0; i < all.length; i += 1) {
	        all[i].SourceElement().parentNode.className += ' has-jax';
	    }
	});
	</script>
	<script type="text/javascript" src="http://cdn.mathjax.org/mathjax/latest/MathJax.js?config=TeX-AMS-MML_HTMLorMML"></script>

Can add a preamble with macros at the top of the document
+ Avoid using `\ensuremath{}` and `\providecommand`