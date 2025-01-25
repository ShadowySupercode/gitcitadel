## Drumroll, please....

In a previous article, I introduced the concept of [relay communities](nostr:naddr1qvzqqqr4gupzplfq3m5v3u5r0q9f255fdeyz8nyac6lagssx8zy4wugxjs8ajf7pqydhwumn8ghj7argv4nx7un9wd6zumn0wd68yvfwvdhk6tcpr3mhxue69uhhg6r9vd5hgctyv4kzumn0wd68yvfwvdhk6tcqp5cnwvesxcunjwpcxymrsvgwmj66e).

The ink had barely dried, on that set of instructions, before one of my favorite Nostr devs, [ثعبان](nostr:nprofile1qythwumn8ghj7enjv4h8xtnwdaehgu339e3k7mf0qy88wumn8ghj7mn0wvhxcmmv9uqzqla9dawkjc4trc7dgf88trpsq2uxvhmmpkxua607nc5g6a634sv598gk68), rolled out the alpha version of a relay-community client.

![chachi for nos.lol](https://i.nostr.build/iwVwUUXfiAj7pSMa.png)

Obviously, it's still a bit of a construction site, but you can check out how it'd work, for your community, by test-driving the functionality on your own relay. Simply type _https://chachi.chat/_ followed by the name of your relay. For instance, one gigantic relay community, where nearly everyone can try out the functionality, is [nos.lol](https://chachi.chat/nos.lol).

If your relay community does not require AUTH to read, anyone can pull your chatter into their own relay and respond to it there. That is because every chat entry is simply a kind 09 event, and unprotected events are not private data.

For instance, I moderate one community [theforest.nostr1.com](https://chachi.chat/theforest.nostr1.com), that is openly readable, and that's probably where most of the chatter on [nostr.band](https://chachi.chat/relay.nostr.band) is coming from, as that relay is an aggregator of the content of many other relays. However, I have another community, [gitcitadel.nostr1.com](https://chachi.chat/gitcitadel.nostr1.com) that is AUTH-protected, whose content stays private to those allowed on that relay. Communities are where write-protected and AUTH relays are going to really shine, as they create an environment similar to Telegram, but where you control the dataset, you decide which types of events to support, and you design the client, the algos, the moderation, the visibility, etc.

With communities, **the onboarding experience is seamless**: just get a browser extension and a nsec, login, start writing and posting, and _start receiving responses_. Active, chatty, well-moderated communities will be more attractive to onboard to, than chaotic, spammy, or empty communities. This means that you don't have to have the killer entry under "Posts" (where kind 11 and eventually kind 01 posts appear), just to get some interaction. Chat is the Great Equalizer.

So, we're testing both setups, with [cloudfodder](nostr:nprofile1qyghwumn8ghj7mn0wd68ytnhd9hx2tcpzfmhxue69uhkummnw3eryvfwvdhk6tcqyp7vx29q3hdj4l0elxl800hlfjp538le09epsf7k9zj59ue2y37qu84upun) adjusting the relay faucet code and ثعبان is fiddling with the community client settings, to make the most-comfortable situation for both kinds.

![The beginning has ended.](https://quotefancy.com/media/wallpaper/3840x2160/361833-Winston-Churchill-Quote-Now-this-is-not-the-end-It-is-not-even-the.jpg)

## This is the signal

This #Chachi client, of course, is merely the first horse out of the gate. There are already other devs hacking away at variants of the same concept, such as [#Flotilla](https://flotilla.coracle.social/), I'm sure CloudFodder is also cooking, later versions of #Alexandria will integrate theforest community, and etc. etc. etc.

It remains to be seen, how many new use cases can be dreamt up, with this new architecture, but I am quite certain, that this is the beginning of the end of Nostr 1.0. We are moving up and out, and away from the stultifying and limiting concept of Twitter 2.0, toward 

![The OtherStuff.](https://i.nostr.build/nToghxbBIzNLx27t.jpg)

Soon, we will enter Nostr 2.0. See you on the other side.