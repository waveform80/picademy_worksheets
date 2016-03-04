#!/usr/bin/env python3

import io
import os
import errno
import subprocess
from collections import namedtuple
from xml.etree import ElementTree as et
from copy import deepcopy

GroupBox = namedtuple('GroupBox', ('x', 'y', 'width', 'height'))

NS = {
    "dc":       "http://purl.org/dc/elements/1.1/",
    "cc":       "http://creativecommons.org/ns#",
    "rdf":      "http://www.w3.org/1999/02/22-rdf-syntax-ns#",
    "svg":      "http://www.w3.org/2000/svg",
    "sodipodi": "http://sodipodi.sourceforge.net/DTD/sodipodi-0.dtd",
    "inkscape": "http://www.inkscape.org/namespaces/inkscape",
    }
for prefix, url in NS.items():
    et.register_namespace(prefix, url)

SOURCE = 'SOURCE.svg'
DATA = {
    _id: GroupBox(float(x), float(y), float(width), float(height))
    for line in subprocess.check_output(['inkscape', SOURCE, '--query-all']).decode('ascii').splitlines()
    for (_id, x, y, width, height) in (line.strip().split(','),)
    }

with io.open(SOURCE, 'rb') as source:
    original = source.read()
    doc = et.fromstring(original)
    page_group = doc.find('svg:g', NS)
    template = deepcopy(doc)
    del template.find('svg:g', NS)[:]

for folder_group in page_group.findall('svg:g', NS):
    folder_id = folder_group.attrib['id']
    try:
        os.mkdir(folder_id)
    except OSError as e:
        if e.errno != errno.EEXIST:
            raise
    for image_group in folder_group.findall('svg:g', NS):
        image_id = image_group.attrib['id']
        filename = os.path.join(folder_id, '%s.svg' % image_id)
        output_doc = deepcopy(template)
        output_doc.attrib['width'] = str(DATA[image_id].width)
        output_doc.attrib['height'] = str(DATA[image_id].height)
        output_root = output_doc.find('svg:g', NS)
        output_root.attrib['transform'] = '%s translate(%f,%f)' % (
                output_root.attrib.get('transform', ''),
                -DATA[image_id].x, -DATA[image_id].y)
        output_root.append(deepcopy(image_group))
        with io.open(filename, 'wb') as output:
            output.write(et.tostring(output_doc))
        subprocess.check_call(['inkscape', filename, '--vacuum-defs', '-l', filename])

