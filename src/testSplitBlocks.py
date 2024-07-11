import unittest

from splitblocks import MDtoBlocks
from splitblocks import blockType


class TestSplitBlocks(unittest.TestCase):
    def test_eq(self):
        md = """This is **bolded** paragraph

This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line

* This is a list
* with items
"""

        output = ["This is **bolded** paragraph",
                  """This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line""",
                  """* This is a list
* with items"""]

        md1 = """This is **bolded** paragraph 

This is another paragraph with *italic* text and `code` here 
This is the same paragraph on a new line 

* This is a list
* with items
"""

        output1 = ["This is **bolded** paragraph",
                   """This is another paragraph with *italic* text and `code` here
This is the same paragraph on a new line""",
                   """* This is a list
* with items"""]

        self.assertEqual(MDtoBlocks(md), output)
        self.assertEqual(MDtoBlocks(md1), output1)


paragraph = "paragraph"
heading = "heading"
code = "code"
quote = "quote"
ul = "ul"
ol = "ol"


class TestBlockType(unittest.TestCase):
    def test_eq(self):
        inputs = [blockType("## Heading"),
                  blockType("```code```"),
                  blockType("> lksajdf\n> jlsd"),
                  blockType("* al;skdjf\n* laskdfj"),
                  blockType("- laskdfj\n- ;alsdkfj"),
                  blockType(". ladskjf\n. alsdjf"),
                  blockType("> alsdkfj\nsadkjlj\n. sdlf")]
        outputs = [heading, code, quote, ul, ul, ol, paragraph]
        self.assertEqual(inputs, outputs)


if __name__ == "__main__":
    unittest.main()
