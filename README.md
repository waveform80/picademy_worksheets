# Picademy Worksheet Template

The template for the creation of worksheets is in `template.sla`. This is
inteded for usage with Scribus 1.4.x.

## Master Pages

* **Blank** - intended for entirely blank or freeform pages.

* **Normal** - for regular pages. This places a Picademy logo at the top-left
  of the page and reserves space for the title and description boxes to the
  right of it. A guide is provided to align images with the logo if required,
  and the footer includes the required copyright information.

## Paragraph Styles

* **Heading** - this is intended for headings within the body copy. The font is
  Bebas Neue which can installed from the `bebas_neue.zip` archive in the same
  directory as the template. The style includes pre-paragraph spacing.

* **Default Paragraph Style** - use this for regular text within the body.
  Pre-paragraph spacing and optical margins are included. Justification is full
  excluding the trailing line.

* **List Level 1** and **List Level 2** - use these for lists (bulleted or
  numbered) within the body. The initial tab-stop is placed for separation
  between the list symbol/number and the list entry.

* **Code** - use this for code blocks within the body but *not* for inline code
  examples (see character styles below).

## Character Styles

* **Command** - use this for inline code examples within default paragraph
  text. The font will be switched to Courier New (monospaced) and underlined
  to emphasize the distinction between the code and any trailing punctuation
  like full stops.

* **Keyword** - use this for keywords within code blocks. The bold variant of
  the parent font will be used and the color will be switched to a mild blue.

* **String** - use this for string literals within code blocks. The font
  will be switched to a light blue.

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
