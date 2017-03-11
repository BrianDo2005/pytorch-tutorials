from docutils.parsers.rst import Directive
from docutils.statemachine import StringList 
from docutils import nodes
import re
import os
import sphinx_gallery

class IncludeDirective(Directive):

    # defines the parameter the directive expects
    # directives.unchanged means you get the raw value from RST
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = False
    add_index = False

    docstring_pattern = r'"""(?P<docstring>(?:.|[\r\n])*?)"""\n'
    docstring_regex = re.compile(docstring_pattern)

    def run(self):
        document = self.state.document
        env = document.settings.env
        rel_filename, filename = env.relfn2path(self.arguments[0])

        text = open(filename).read()
        text_no_docstring = self.docstring_regex.sub('', text)

        code_block = nodes.literal_block(text=text_no_docstring)
        return [code_block]


class GalleryItemDirective(Directive):
    required_arguments = 1
    optional_arguments = 0
    final_argument_whitespace = True
    has_content = False
    add_index = False

    def run(self):
        args = self.arguments
        fname = args[-1]
        basename = os.path.basename(fname)
        dirname = os.path.dirname(fname)

        intro = sphinx_gallery.gen_rst.extract_intro(fname)
        thumbnail_rst = sphinx_gallery.backreferences._thumbnail_div(dirname, basename, intro)
        thumbail = StringList(thumbnail_rst.split('\n'))

        thumb = nodes.paragraph()
        self.state.nested_parse(thumbail, self.content_offset, thumb)

        return [thumb]