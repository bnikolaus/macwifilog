macwifilog
==========

I put a log wrapper around the airport apple command as it was the only thing I could find that would give me
the specifics of how wireless is performing. I am using this to debug some wireless outages we are having at 
puppetlabs. This was a quick hack so be nice.

The reason it needs your password is becaue I created a soft link which require's sudo access.

Command
sudo ln -s /System/Library/PrivateFrameworks/Apple80211.framework/Versions/Current/Resources/airport /usr/bin/airport



