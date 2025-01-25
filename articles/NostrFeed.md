## Unsucking the feed is real

As a Nostrich with an interesting, thought-provoking, and informative feed... a feed so good, that we're creating clients just to look at that feed... a feed that puts a lie to the idea that Nostr is nothing, but people reposting from Twitter or rehashing worn-out Bitcoin memes... a feed that I personally and increasingly enjoy perusing... I am here to tell you that the feed is real.

![Yes, it's real.](https://i.nostr.build/eXAINZP6UjWTDnCA.jpg)

It's taken me over a year, to produce this feed. I literally spent hours and hours, day in and day out, scouring the Nostrverse for people worth introducing other people to. It was brutally difficult, as I was fighting the inherent nature of the Nostr clients and relays, in their current, most-popular form.

## It goes like so...

Here are the steps I took, that sometimes weren't possible to take, until I tried to take them, and that still will sometimes break your client because the clients are often _intentionally_ designed to steer you into having one particular feed:

1) **Make a screenshot** of your current relay list and copy your follows list.
2) **Unsubscribe from all the relays**, that you are currently subscribed to. Your feed should disappear. If it doesn't, or it doesn't allow for this, switch to a different client app because yours is corrupted.
3) **Unfollow everyone.** Delete the whole list. You are taking your follows private, which will invariably result in only following npubs whose stuff you actually want to see, since there's no longer any virtue-signaling going on. Also, it's easier to explain having no list, than a very short one. If your client doesn't allow for this, or starts throwing error messages and freezing up, then switch to a different client app because yours is corrupted.
4) **Curate your copied follows list.** Go line by line and look at the feed produced by the npub on that list.
   * Do you want to see that in your feed, going forward?
    * Do they produce original content and/or are they interesting conversationalists, in the replies?
    * Have they been active, within the past three months?
    * Are they simply good friends or real-life acquaintances, that you want to keep tabs on?
    * If not, cross out their name.
    * If you have been following someone because they repost or quote interesting things, **look at who they've been reposting** and follow them, instead.
5) Of the npubs remaining on your list, go through and select the 10 most interesting ones, and **look at the reposts and quotes** in their feed, and their topical lists like \"Favorites\", \"Devs\", \"Recipes\", etc. (Not their follows list, unless it's quite short, as follows tend to be full of people they follow for social-signaling or client-functional reasons, that they don't actively look at.) Find some new follows, there.
6) Now, set up a personal relay and add all the follows, that made the cut, to **your allowed-npubs list**. Do not add people to the list, just to make them feel better, or because you feel guilty, as they follow you, or to keep them from yelling at you. Remember, they can't see the list!
7) Think about the topics you find interesting, and add an **allowed-keywords list** (this is better than hashtags, as it searches the entire content of the notes), with the OR operator (these allowed npubs OR these allowed topics).
8) Make sure that you choose words likely to find the content you are most-interested in, and not people just ranting about it or spamming (those are great additions to your relay's block-list). If you are Muslim, for instance, instead of "Islam" or "shariah", choose "hadith" or "riba", as those are words more-likely to be used by people who know what they are talking about. If you are into bread baking, add "sourdough", "rye", "yeast", or "whisk", but don't add "bread" or "carbs". Once a note from those people shows up in your feed, and their feed looks like someone interesting, you can add their npub to your allow list. Remember: **The topics are there to find people to add to the allow list**, not merely for their own sake, as this is not a topical relay, but a personal one.
9) Open up a faucet (or relay syncing) with some of the big relays you previously unsubscribed from, some WoT relays, and some of the paid relays (nostr.land, nostr.wine, nostr21.com, and sovbit.host, for example). **Your relay will filter that feed** and only accept the events from the people and topics on your list. As your relay becomes more popular, npubs will begin writing directly to it, and the connections to other relays will sink in significance.
10) Go to your client of choice and **subscribe to your new relay**. Also subscribe to some topical relays, or curated neighborhood relays, you find interesting or your frens are running. This is an easy way to find new, interesting npubs, to add to your own relay.

![The end](https://i.pinimg.com/564x/e4/32/fc/e432fc1ce1fc8a5077e33290ec15e0ce.jpg)

That's a lot of work, you say? Yes, but the result is great, and you are now fully in-charge of your own feed. You also -- here's the cool part -- have a feed good enough, that other people can add your feed to theirs and enjoy your manual curation. As you refine and expand your feed, theirs will also be refined, in parallel. You are now an official Nostr Community Curator. My sincere congratulations.

![Certificate](https://i.nostr.build/FDtR0Z5VAJTxCGHL.png)

## Why is this so hard?

This is only a lot of work because the clients aren't designed to interact with relays, to this extent, as they were created to service mega-relays, download all their crap to your local cache, and adjust the feed over the follows/mutes lists. This was an idea borne of the axiom that Relays Are Hard, so there will only ever be a handful of them, where we'd all clump together and the relay operators would never judge the quality of someone's content. Then, some unusually clever people made relays increasingly easy, and the mailbox communication model was invented, and here we are.

What we have now, and that is slowly growing in popularity, among the #NostrIntelligentsia, are Nostr clients aimed at curating and viewing individual relays or personalized sets of smaller or more-specialized relays. The reigning client devs refused to give us those clients, and most of us aren't up to developing our own clients, so the relay devs took matters into their own hands and made the clients themselves. The free market remains undefeated.

This is a total game-changer. Last one to board this train is a rotten egg.

Originally, relays were supposed to be completely stupid and clients were supposed to be completely smart, but it's now actually the other way around, because most relay devs have a market-born incentive to make their content highly customizable and appealing to individuals (so that more people run relays).

## But what about algos?

Can't you just slap an algo on top of Damus, Lol, or Primal relays, and get the same result? I would argue... no. No, you can't. Or, rather, only in the short to medium term.

Running your own relay, is running your own server. You are now _intellectually independent_, at a machine-level, and therefore a fully sovereign consumer. If you then use algos to control your own server, or in a client that subscribes to your own server, then you can further-refine a feed that is already in a high-to-you-signal state, rather than risking an algo inching you toward the Consensus Feed.

I have noticed that my own feed is slowly drifting away from the ReplyGuy-Cryptobot-Porny-Bitcoin-Meme Dumpster Fire, that almost everyone else is looking at, and it's due to running my own relay. If I use DVMs, those algos sometimes refer to relays I intentionally avoid, so they return results according to those relays. The results are as underwhelming, as you would expect, and often are simply 31 flavors of the Trending List.

But, that isn't your problem, anymore.
From here, you can actively expand and refine your feed, over your whitelist, the topics, and your personally-managed algos.

Happy Nostr-ing!