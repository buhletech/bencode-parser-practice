*Bencoding From Scratch (Learning Project)*

  A hand-written Python implementation of Bencoding (the encoding format used by BitTorrent), built purely as an exercise to understand string parsing, indexing, and recursive data formats.

*Purpose*

  This project is not intended to be a production ready or optimized bencoding library. There are already mature, well-tested libraries that should be used for any real-world application.

  The goal here was purely educational: To build an intuition for manual string parsing using indices and pointers how length-prefixed formats avoid ambiguous delimiters recursive parsing of nested data structures (lists and dictionaries containing other lists/dictionaries)

*What is Bencoding?*

  Bencoding is a way to specify and organize data in a terse format. It is the encoding used by the peer-to-peer file sharing system BitTorrent for storing and transmitting loosely structured data. It supports the following types: byte strings, integers, lists, and dictionaries.
  Bencoding is most commonly used in torrent files, and as such is part of the BitTorrent specification. These metadata files are simply bencoded dictionaries.


*Structure*
  bencode_int.py — decodes bencoded integers
  bencode_string.py — decodes bencoded strings
  bencode_list.py — decodes bencoded lists (of strings and integers)
  bencode_dict.py — decodes bencoded dictionaries (including string, integer, and list values)

  Each file can be run directly to test a single input from the console.

*Disclaimer*

  This code was written as a learning exercise while studying parsing techniques. It has not been rigorously tested against edge cases and should not be used as a reference implementation of the Bencoding spec.
