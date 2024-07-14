# The new Great Library

We have all heard tales of Amazon or other booksellers banning customers from their bookstores or censoring/editing purchased books. The famous [Project Gutenberg](https://www.gutenberg.org/), and similar organizations, are performing a good work, to help protect many of our precious books from this fate, but it is merely a centralized website and therefore not censorship resistant. Also, it mostly posts books in English or German.

So, we at nostr:npub1s3ht77dq4zqnya8vjun5jp3p44pr794ru36d0ltxu65chljw8xjqd975wz have decided to move Project Gutenberg to Nostr and house it in the most distributed way possible: on relays. Specifically, our new, public [Citadel relay](https://thecitadel.nostr1.com/) for out-of-print books (and other documents), but also on any relay, anywhere.

And, because we are a very humble group, we're naming the effort "Alexandria". And the first book to be printed on Nostr is the Bible because *obviously*.

## Why on relays?

Well, why not on relays? Relays are one of the few widely-distributed databases for documentation in existence. The relay database spans the entire globe and anyone can maintain their own relay on their personal computer or mobile phone. 

That means that anyone can house *their own* books.
Which books are their own? Any books they have in their own possession. Any books someone would have to physically pry out of their cold, dead, computer.

## Notes are perfect for publishing 

Once we begin generating eBooks from notes with an associated header (which will be quite easy to do, so long as they are written in markdown or similar), they will also be readable, downloadable, and storable in ePub format (see [Pandoc](https://pandoc.org/epub.html)). And it is, after all, only a matter of time until someone enterprising makes an ePaper Nostr client for calmer reading of notes, and then you can download and read them, without having to bother converting beforehand, which maintains their Nostr-navigation.

The new event kind [30040](https://wikifreedia.xyz/nkbip-01/) allows us to take any sort of note containing any sort of characters and create a type of "note collection" or "book of notes", "journal of notes", "magazine of notes". And it can be nested or embedded in other notes, creating any sort of note-combination and note-hierarchy you can think of, only limited in size by the ability of your computer to processes the relationships.

## Save the Zettels

The associated kind 30041 adds the prospect of breaking longer texts or articles up into sections or snippets (called "Zettel" in German). We can then collect or refer to particular bits of a longer text (like a chart, elegant paragraph or definition, data table), directly. Anyone can create such snippets, even of texts they didn't write, as they can add a reference to the original publication in the tags of the new event.

This means we no longer have to "copy-paste" or quote other people's works, we can simply tie them in. If we worry about them being deleted, we can fork them to create our own, digitally-linked version, and then tie that in. This means that source material can be tied to the new material, and you can trace back to the source easily (using Nostr IDs and tags, which are signed identifiers) and see who else is branching out from that source or discussing that source.

## It's gonna be HUGE!

We are making a big, beautiful library... and you are going to build it for us. Anyone, anywhere can therefore publish or republish any document they wish, with Nostr, and store it wherever they have a relay, and view it on any client willing to display it.

You will own something and be happy.
