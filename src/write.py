import sqlite3
from datetime import date

from textual.app import ComposeResult
from textual.widgets import Static, Input, TextArea

from database import add_entry, update_tag, update_all, update_content
from constants import DB


class Write(Static):

    def __init__(self):
        super().__init__()
        self.i = 0
        self.t = ""
        self.c = ""

    def compose(self) -> ComposeResult:
        tag = Input(placeholder="Tag", id="tag", valid_empty=False)
        #tag.border_title = "Tag11"
        yield tag
        #yield Input(placeholder="Content", id="content", valid_empty=False)
        yield TextArea()

    def on_mount(self):
        text = self.query_one(TextArea)
        text.tab_behavior = "indent"
        text.tooltip = "Please enter your journal here"
        #text.read_only = True
        #log.error(text.document.newline)

    def submit(self):
        content = self.query_one(TextArea).text
        dt = date.today()
        tag = self.query_one(Input).value

        if content == "" or tag == "":
            return

        with sqlite3.connect(DB) as conn:
            add_entry(conn, (tag, dt, dt, content))

        self.query_one(TextArea).text = ""
        self.query_one(Input).value = ""

    def to_view(self, i, tag, content):
        self.i = i
        self.t = tag
        self.c = content
        t = self.query_one(Input)
        t.value = tag
        c = self.query_one(TextArea)
        c.text = content
        #c.read_only = True

    def to_update(self):
        t = self.query_one(Input).value
        c = self.query_one(TextArea).text
        d = date.today()
        i = self.i

        with sqlite3.connect(DB) as conn:
            if t != self.t and c != self.c:
                #log.error("IF IS WORKING")
                data = [t,d, c, i]
                update_all(conn, data)
            elif t != self.t:
                data = [t,d,i]
                update_tag(conn, data)
            elif c != self.c:
                data = [d,c,i]
                update_content(conn, data)

