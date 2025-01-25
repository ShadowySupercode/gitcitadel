# My suggestion for scaling up and staying humble

## The original protocol design was \"good enough for now\"

When Nostr was invented and got started with developing implementations, the *Original Devs* (ODs) were convinced this was going to be big... maybe... someday... hopefully.

But, whatever they did at the moment should definitely scale up a bit and be a bit flexible, to attract innovators and keep up the momentum. So, they designed the protocol to be open and left the specifications a bit vague and very high-level, so that nobody was forced into a particular implementation, in order to adhere to the spec. And they put the specs into a GitHub repository and managed them by a committee of collaborators, who were generally open to changes to the specs, including breaking changes.

That was smart. And it was \"good enough for now\"... back then. After all, Nostr (and the associated wiki and modular article specs) hadn't been invented, yet, so they couldn't write the protocol in the protocol before the protocol existed. They're good, but not _that_ good.

What they specifically wrote, into the [Nostr Protocol](https://github.com/nostr-protocol/nips) was:
 
> To promote interoperability, we standards (sic) that everybody can follow, and we need them to define a **single way of doing each thing** without ever hurting **backwards-compatibility**, and for that purpose there is no way around getting everybody to agree on the same thing and keep a centralized index of these standards...
> Standards may emerge in two ways: the first way is that someone starts doing something, then others copy it; the second way is that someone has an idea of a new standard that could benefit multiple clients and the protocol in general without breaking **backwards-compatibility** and the principle of having **a single way of doing things**, then they write that idea and submit it to this repository, other interested parties read it and give their feedback, then once most people reasonably agree we codify that in a NIP which client and relay developers that are interested in the feature can proceed to implement.

# I disagree with this statement.

I don't disagree with what they _meant_, or what they _wanted_, I disagree with what they specifically wrote.

Standards (defined as prose specifications) are not the only -- or even best -- way to ensure interoperability or to check for backwards-compatibility. And, as they later note, basing a protocol off of implementations is arguably worse (but faster) than using specifications, as implementations have a life of their own and are sometimes simply shoddy or buggy, their content eventually differs from what ends up in the final standard, or there are soon multiple implementations covering the same spec \"in theory\", but not in practice, so that their events are incompatible.

And then the inevitable, heated discussion begins: 
* Which implementation is the Real Standard™?
* Who controls the Real Standard™?
* How is the Real Standard™ spec supposed to be written?
* Does everything have to be in the same file type or markup language? If not, how can we ensure compatibility?
* What is realistic content for the data files?
* Is the Real Standard™ including all of the information needed to ensure interoperability, but not anything more, without reducing innovation and artificially forcing consensus by encouraging copy-paste or forking of product code?

## There is a third way: write the test first

We actually do not need standards to define a single way of doing each thing. A *test* is another way, and I think it is the best (i.e. the most-efficient and most-effective) way.

Specifically, I think we can borrow the simple behavior-driven design (BDD) language called Gherkin (or something similar), which is used to write dynamic specifications:  i.e. implementations that test adherence to a set of rules, rather than an implementation that uses the rules to perform some task for an end user.

Gherkin simply allows you to create standard scenarios and test data and write the tests up in a way that can be performed manually or through automation. For example ( [source](https://www.pragmaticapi.com/blog/2013/01/21/bdd-atdd-for-your-agile-rest-api-part-2/) ):
![Gherkin example](https://res.cloudinary.com/jhrmn/image/upload/v1362658828/groovy_cucumber_twitter_lpg6yj.png)

(For a concrete example of such a TDD Protocol for Nostr, please see the [nostr-voliere repo](https://github.com/schmijos/nostr-voliere/tree/main/features) from nostr:npub1axy65mspxl2j5sgweky6uk0h4klmp00vj7rtjxquxure2j6vlf5smh6ukq .)

## This really is better

This TDD Protocol design would have some downsides and some upsides, of course, like any change.

### Downsides
* You can't write a TDD spec by yourself unless you understand basic software functionality, how to define an acceptance test, and can formulate a use case or user story.
* The specs will be more informative and agnostic, but also longer and more detailed.
* Someone will have to propose concrete test data (i.e. a complete json event) and spec interlinking will be explicit, rather than writing \"...\", \"etc.\", or \"sorta like in that other section/doc, but not really\" all over the place.
* The specs will tend to focus on positive cases, and leave off error-handling or most edge-cases, so developers can't use them to replace unit tests or other verification of their product.

### Upsides
* The specs will be concrete and clear, in a type of pseudocode, while leaving the actual implementation of any feature up to the individual developer, who uses the spec.
* The specs will be orderly and uniquely-identifiable, and can have hierarchy and granularity (major and minor tests, optional tests, tests only under certain conditions, etc.)
* Deciding whether changes to the spec are breaking changes to the protocol would be simple to determine: Does the previous test still pass?
* Specs will always be final, they will simply be versioned and become more or less defined over time, as the tests are adjusted.
* Product developers will feel less like they \"own\" particular specs, since their implementation is actually what they own and the two remain permanently separate.
* Developers can create an implementation list, defining specific tests in specific versions, that they adhere to. This makes it more transparent, what their product actually does, and lowers their own documentation burden.
* Rather than stalking the NIPs for changes, or worrying about what some other implementation someplace has built, developers can just pull the repo and try running the relevant tests.
* Each product developer can test the spec by trying to perform or automate/run it, and request changes to ensure testability, raising the quality of the spec review process.

This is already a lot to think about, so I'm just going to end this here.
Thank you for reading.