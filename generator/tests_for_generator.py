import unittest
from generator.md_gen import MdSource
from generator.md_gen import read_md
from generator.md_gen import prepare_data_to_write
from generator.md_gen import read_txt
from generator.md_gen import write_to_file

class TestSource(unittest.TestCase):

    def test_lnk(self):
        md = MdSource(*read_txt('in.txt'))
        expect_lnk = '+ [Reverse String](#reverse-string)'

        self.assertEqual(md.get_md_link(), expect_lnk)

    def test_title(self):
        md = MdSource(*read_txt('in.txt'))
        expect_title = '## Reverse String'
        self.assertEqual(md.get_md_title(), expect_title)

    def test_code(self):
        md = MdSource(*read_txt('in.txt'))
        expect_code = """```python
s.reverse()
```
"""
        self.assertEqual(md.get_md_code(), expect_code)

    def test_task(self):
        md = MdSource(*read_txt('in.txt'))
        expect_task = """## Reverse String

https://leetcode.com/problems/reverse-string/

```python
s.reverse()
```

"""
        self.assertEqual(md.get_md_task(), expect_task)


class TestWriting(unittest.TestCase):
    def test_write_to_file(self):
        expect_data = """# STRING
+ [Reverse String](#reverse-string)
<!---->
## Reverse String
https://leetcode.com/problems/reverse-string/
```python
s.reverse()
```"""
        md = MdSource(*read_txt('in.txt'))
        s = read_md('out.md')
        s = prepare_data_to_write(md, s)
        write_to_file('out.md', s)

        with open('out.md') as f:
            data = f.read()
        self.assertEqual(data, expect_data)