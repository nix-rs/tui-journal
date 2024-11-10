# Main App File

import sqlite3

from textual.app import App, ComposeResult
from textual.widgets import Footer, TabPane, TabbedContent

from database import db, delete_entry
from read import Read
from write import Write
from constants import DB



class Journal(App):
    ENABLE_COMMAND_PALETTE = False
    CSS_PATH = "style.tcss"

    BINDINGS = [
        ("d", "toggle_dark", "Dark Mode"),
        ("q", "quit", "Quit"),
        ("a", "submit", "Add"),
        ("u", "update", "Update the entry"),
        ("v", "view", "View the entry"),
        ("r", "remove", "Remove the content"),
        ("s", "sorts", "Sorting"),
    ]

    def compose(self) -> ComposeResult:
        with TabbedContent("Read", "Write"):
            with TabPane("Read", id="read"):
                yield Read()
            with TabPane("Write", id="write"):
                yield Write()
        yield Footer()

    def action_remove(self):
        data = self.query_one(Read).select()
        with sqlite3.connect(DB) as conn:
            delete_entry(conn, data[0])

    def action_update(self):
        wrt = self.query_one(Write)
        wrt.to_update()

    def action_view(self):
        self.query_one(TabbedContent).active = 'write'
        data = self.query_one(Read).select()
        write = self.query_one(Write)
        write.to_view(data[0],data[1], data[4])

    def action_submit(self) -> None:
        write = self.query_one(Write)
        write.submit()

    def action_toggle_dark(self) -> None:
        self.dark = not self.dark
