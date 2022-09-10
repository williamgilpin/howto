
On the remote computer, go into System Preferences > Sharing and check the boxes to allow remote login and remote management

Find the remote computer's hostname

	hostname

This will be something like xxxx-55-555-55-5.university.edu. On the local computer, run

	ssh hostname

And enter the admin password when prompted. Or, to access a single account,

	ssh username@hostname

### Change the remote hostname

I could not get this working on macOS. I found [one related StackExchange thread](https://superuser.com/questions/1103353/changing-hostname-for-remote-login-on-a-mac), but there is no working solution yet

