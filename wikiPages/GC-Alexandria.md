![Roman scrolls](https://raw.githubusercontent.com/ShadowySupercode/gitcitadel/master/logos/GC-Alexandria.png)

# GC Alexandria

Alexandria is a Nostr Knowledge Base (NKB) and a reader for long-form articles. It is produced by the [GitCitadel](https://gitworkshop.dev/r/naddr1qq9xw6t5vd5hgctyv4kqzrthwden5te0dehhxtnvdakqyg8ayz8w3j8jsduq492j39hysg7vnhrtl4zzqcugj4m3q62qlkf8cypsgqqqw7vsfd6ccp) development cooperative (please see [[GitCitadel-docs]]).

## History of the project

Alexandria was originally named "indextr" and was conceived by [Liminal](https://njump.me/npub1m3xdppkd0njmrqe2ma8a6ys39zvgp5k8u22mev8xsnqp4nh80srqhqa5sf) to work as a NKB, in particular for scientific or engineering journals and publications.

It was quickly noticed that the same event types (30040 and 30041) could be used to produce eBooks and any other collection of individual articles/pages, so the GitCitadel team decided to take on the project and adapt it to create the [Alexandria eReading web app](https://habla.news/u/laeserin@getalby.com/1719204947236), in order to publish out-of-copyright books, starting with the Bible.

## Web client

### Elegant Design

As Alexandria is targeted toward those who are trying to focus on longer, more-complex content, the design has been stripped down of any distracting elements or unnecessary details, so that the user can concentrate on the valuable information stored in the documents that they are viewing. Both light-mode and dark-mode are available.

![Menu](https://i.nostr.build/4oAlm.png)

![event display](https://i.nostr.build/KG2D2.png)

![cards](https://i.nostr.build/Vwkl0.png)

### Modular articles

The specialty of this client is the ability to display long-form articles, particularly of the modular variety: event kinds 30040 and 30041 from [[nkbip-01]]. It is also able to display wiki pages (event kind 30818 from [[nip-54]], and normal long-form articles of event kind 30023 from [[nip-23]].

Modular articles are often referred to as the *Nostr eBook format*, with 30040 events containing the metadata and the ordered list of the 30041 notes, which contain the markdown-formatted content.

### Write articles

Alexandria features a markdown-upload facility, for you to transform your well-formatted text to Nostr events and publish them to your preferred relays. The GitCitadel relay is set as the default, to ensure that you have at least one relay that is sure to work.

Simply make sure to structure the article content like so:

```
# title (mind the space)

## topic1

text that you want displayed as content

## topic2

more text

```

Until this feature is completed, you can use the upload facility called [eBookUtility](https://gitworkshop.dev/r/naddr1qqxx2sn0da442arfd35hg7gpz4mhxue69uhhqatjwpkx2un9d3shjtnrdaksyg8ayz8w3j8jsduq492j39hysg7vnhrtl4zzqcugj4m3q62qlkf8cypsgqqqw7vs555whg).

### Project repo

The project repo has been published to Nostr using Ngit and is viewable at [GitWorkshop](https://gitworkshop.dev/r/naddr1qq9yzmr90pskuerjd9sszrthwden5te0dehhxtnvdakqyg8ayz8w3j8jsduq492j39hysg7vnhrtl4zzqcugj4m3q62qlkf8cypsgqqqw7vszahgpn/).

The repo address is:
nostr:naddr1qq9yzmr90pskuerjd9sszrthwden5te0dehhxtnvdakqyg8ayz8w3j8jsduq492j39hysg7vnhrtl4zzqcugj4m3q62qlkf8cypsgqqqw7vszahgpn

### Software releases

Please see the roadmap in the [[GitCitadel-docs]] for the estimated delivery of the next version.

![Alexandria v1.0 Work Breakdown Structure](https://raw.githubusercontent.com/ShadowySupercode/gitcitadel/master/plantUML/Alexandria/Alexandria_v1.png)
