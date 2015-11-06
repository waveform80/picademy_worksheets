# Contributing

The template for the creation of worksheets is in `template.sla`. This is
inteded for usage with Scribus 1.4.x. Install pre-requisites on Ubuntu with
the following command:

	sudo apt-get install scribus ttf-mscorefonts-installer fonts-roboto \
		texlive-fonts-recommended fonts-freefont-otf

You will also need to install the Bebas Neue font from the `bebas_neue.zip`
archive in the root of the repository. Simply extract the content and double
click on the font to open the Gnome font installer, then click "Install" at
the top right of the window. This will install it as a user font (not system
wide).

## Master Pages

* **Blank** - intended for entirely blank or freeform pages.

* **Normal** - for regular pages. This places a Picademy logo at the top-left
  A guide is provided to align images with the logo if required, and the footer
  includes the required copyright information.

## Paragraph Styles

* **Heading** - this is intended for headings within the body copy. The font is
  Bebas Neue which can installed from the `bebas_neue.zip` archive in the same
  directory as the template. The style includes pre-paragraph spacing.

* **First Paragraph** - use this for the first paragraph in an article. It uses
  a two line drop-cap but is otherwise identical to the default from which
  it derives.

* **Default Paragraph Style** - use this for regular text within the body.
  Pre-paragraph spacing and optical margins are included. Justification is full
  excluding the trailing line. The layout engine is given a little wiggle room
  by reducing the minimum glyph width to 95%.

* **List Level 1** and **List Level 2** - use these for lists (bulleted or
  numbered) within the body. The initial tab-stop is placed for separation
  between the list symbol/number and the list entry.

* **Code** - use this for code blocks within the body but *not* for inline code
  examples (see character styles below). This style uses Free Mono (a
  monospaced font).

* **Callout Heading** - use this as the title style for callout boxes. The
  font is a slightly smaller Bebas Neue in white, so it's assumed you've got
  a solid background box behind the title.

* **Callout** - use this for callout content. It's the same as the default
  paragraph style with a slightly smaller font. Callouts typically use a two
  column layout internally when they span the width of the page.

## Character Styles

* **Command** - use this for inline code examples within default paragraph
  text. The font will be switched to Free Mono (as in **Code** blocks) with
  an underline to emphasize the difference between the command and surrounding
  punctuation marks (like full stops).

* **Menu** - use this for inline menu items, e.g. File > Open. Menu items
  should be separated with a right-angled bracket (greater than character).
  This character style uses a bold variant of Roboto Condensed.

* **Keyword** - use this for keywords within **Code** style blocks. The font
  will be switched to a bright orange.

* **String** - use this for string literals within **Code** style blocks. The
  font will be switched to a mild green.

* **Comments** - use this for comments within **Code** style blocks. The font
  will be switched to dull red.

## General Guidelines

* The content of the top box should be 8pt separated from the header and logo.
  I tend to do this quickly by aligning the box to the bottom of the header and
  defining an 8pt margin at the top of the box.

* Call-out boxes have 8pt rounded corners with a similarly shaped contour
  outset by 16pt. The border line is 1pt thick and is darker than the box's
  fill (no standard for the fill though; I should probably define a style for
  the line).

## ICC Color Matching

	$ cd
	$ mkdir -p .color/icc
	$ cd .color/icc
	$ unzip ~/picademy_worksheets/ecirgbv20.zip
	$ unzip ~/picademy_worksheets/eci_offset_2009.zip

The V243H.icc profile can also be installed in ~/.color/icc if you wish, but is
intended for use with an Acer V243H monitor (and it's only a rough profile,
based on a generic TFT profile with some gamma adjustments) so it's probably
useless for most people.

## Font Selection and Design Choices

The trend these days is to use sans-serif fonts even for printed material (I'm
old-fashioned and tend to prefer serifed fonts for such things, but we're
trying to look modern here, so sans it is). The reason for selecting a somewhat
obscure Type 1 font from TeX as the base font (URW Gothic) rather than
something more modern is simply that nothing else seems capable of aligning
drop caps properly (not to mention URW Gothic has a nice wide, rounded style
which is particularly readable).

Code blocks are in Free Mono as this is the default font in IDLE 2 & 3. The
highlighting of strings and keywords is done using colours and styles matching
IDLE's defaults (although not too closely as the defaults don't print well in
black & white). The font's tracking is slightly reduced to give the impression
of smaller text (as in IDLE's defaults) without compromising readability (the
font isn't smaller, just packed a little tighter).

Free Mono is also used for inline code examples to maintain consistency with
code blocks. An underline is used to emphasize the limit of the code and
clearly separate it from surrounding punctuation marks (e.g. trailing full
stops) which otherwise may confuse readers into saving a file with a ".py."
extension. The underline is deliberately offset to ensure it doesn't overlap
with underscores in the text (common in file names and identifiers).

Menu selections are in the bold variant of Roboto Condensed. This is the
default font in Raspbian's LXDE setup (albeit with regular weight) so there
should be some familiarity between the text and what's seen on screen. The
space width is greatly reduced to ensure a block of menu items appears as a
tight sequence.

All graphics in the template use vectors to ensure high quality hard copy. It
is recommended that any bitmap graphics inserted into worksheets have an
effective DPI of at least 200 (the pre-flight verifier is set to check this).

Callout boxes use their own styles for heading and content which are equivalent
to the default style with slightly reduced font sizes. Callouts that span the
page width are expected to use a two-column layout, and all callouts are
expected to have a 4pt margin surrounding text and between columns.

Hints and tips boxes use an 8pt rounded border, with an 8pt margin around
contained text with default font styles. Images *may* use an 8pt rounded border
if appropriate (e.g. images of whole windows typically look silly with a
rounded border). Boxes and images should use contour spacing with the contour
set 8pt out from the frame shape.
