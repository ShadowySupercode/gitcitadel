# NKBIP-01 

[Source](https://github.com/limina1/NKBIPs)

This NKBIP defines the minimum specification required for a Nostr knowledge base (NKB). It also describes possibilities for customizing the events or expanding off from the basic structure. An implementation of event creation can be found in the [[GC-Alexandria]] client.

## Why modular articles?

### Semantic closure

Composable objects that are able to generate self contained meaning given the knowledge they draw from, are referred to as [[Semantic closure]]. When citing an idea, the standard practice is to cite the full text, but this practice fails for longer texts.

Search and navigation: An article may have multiple concepts contained, but they may not be apparent through just the title or summary/abstract. Multiple articles may also contain an explanation of a single concept and individuals may need to read multiple takes on a single concept to understand it.

### Remixability

Instead of writing a unique introduction, take an existing article fragment and use it as a section in your own article.

### Organic structure

A project can encompass many ideas to describe and build. If you want to teach machine learning you may want to pull in concepts from linear algebra, probability, numerical libraries for matrix algebra to fully explain what you are doing and detail the various aspects of your project. An anatomy textbook can link concepts together not only linearly but by anatomical relation. Not only can articles be read linearly but they themselves can be their own sub-network of hyperlinks to related concepts at various levels of organization.

## Implementation

The most basic article can be constructed through two kinds with an analog to the standard kind 0 and kind 1 defined in [[NIP-01]] and influence taken from [[NIP-23]] and [[NIP-54]]:

### 30040: Index

The following rules are **mandatory**:
- There is no ```content``` field.
- The full title of the index or collection MUST be indicated by the ```title``` tag. 
-  The index MUST also be uniquely identifiable using a combination of the ```d``` tag's first value (usually containing the ```title```), the ```pubkey```, and the ```kind``` fields.
-  Kind 30040 is REQUIRED to have events listed in ```e``` tags in the order that they appear in the article. The events may be any already-existing event (including nested kind 30040s).
-  If the index is a derivation or an edit of another event, the pubkey that published the original MUST be indicated by a ```p``` tag, and a reference to the original event MUST be indicated by an ```e``` tag immediately following the ```p``` tag of the originator.

The following rules are **optional**:
- One or more authors MAY be listed in the ```author``` tag.  The ```author``` tag need not correspond to the ```pubkey``` tag of the event originator, as in the case where an npub publishes a public-domain book.  The author of the work, in such a case, is not the owner of the npub that originated the event.
-  The ISBN number of the work MAY be listed in the ```ISBN``` tag.
-  The ```t``` tag MAY be used to define the scope or topic of the index, or to denote hashtags.
-  The ```published_on``` tag MAY be used to define the date on which the collection material was originally published and the ```published_by``` tag MAY be used to define who the publisher was. The ```published_on``` tag should be written in the ISO-8601 date format, as that can handle all dates in recorded history.
-  The ```image``` tag MAY be used to denote a picture to associate with the index.
-  The ```summary``` tag MAY be used to give a short description of the works that the index contains.
-  The ```version``` tag MAY be used to denote the volume, edition, or translation of the work, or the software release that documentation is referring to.

```json
{
	"id": "<event_id>",
	"pubkey": "<event_originator_pubkey>",
	"created_at": <timestamp>,
	"kind": 30040,
    "tags": [
	    [ "d", "<identifier>" ],
	    [ "title", "<full_index_title>" ],
	    [ "author", "<author_name>" ],
	    [ "ISBN", "<ISBN>" ],
	    [ "t", "<topics about which the event might be of relevance>"],
	    [ "published_on", "<date in the format YYYY-MM-DD>" ],
	    [ "published_by", "<publisher of the source material>"],
	    [ "image", "<URL pointing to an image to be shown with the title>" ],
	    [ "summary", "<human readable description of the work>" ],
	    [ "version", "<the volume, edition, or translation included>" ],
	    [ "e", "<event_0_id>", "<relay_0_uri>", ..., "<relay_n_uri>" ],
		[ "e", "<event_1_id>", "<relay_0_uri>", ..., "<relay_n_uri>" ],
		...
		[ "e", "<event_n_id>", "<relay_0_uri>", ..., "<relay_n_uri>" ],
		[ "p", "<pubkey_0>", "<pubkey_1>", ..., "<pubkey_n>" ],
		[ "e", "<original_event_id>", "<relay_0_uri>", ..., "<relay_n_uri>" ]
	],
	"sig": "<event_signature>"
}
```

### Section/Article Note

The following rules are **mandatory**:
- The article MUST contain a ```d``` tag.
- The article MUST contain a ```title``` tag denoting the title of the section ("Introduction", "References", "Chapter 1.0", etc).
- The ```content``` field MUST contain text in **Markdown format**, meant for display to the end user.

Additional optional tags, akin to those for 30040 kind MAY be used.

```json
{
	"id": "5a09d5c2a281c821ae61...",
	"pubkey": "8ae74c618a4713f32129...",
	"created_at": 1708083476,
	"kind": 30041,
	"tags": [
		[ "title", "Events and signatures" ],
		[ "d", "events-and-signatures" ]
	],
	"content": "## Events and Signatures\nEach user has a keypair. Signatures, public key, and encodings are done according to the Schnorr signatures standard for the curve secp256k1.\nThe only object type that exists is the event , which has the following format on the wire:\n...",
	"sig": "49cab8c75fb35cec71d07258..."
}
```

### Labels

This NIP defines the core events for publishing some document. Additional value is added through the curation of documents published, including other npub's documents.

One method for doing this is through labeling (as in [[NIP-32]]). Labels could be used to add metadata to indexes or sections, and also to "externally tag" a particular event for some other use.