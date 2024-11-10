import sqlite3

from textual.app import ComposeResult
from textual.widgets import DataTable, Static
from textual import log

from constants import DB
from database import read_entry

class Read(Static):
    def compose(self) -> ComposeResult:
        yield DataTable()

    def on_mount(self):
        title = ("ID","TAG", "CREATE", "UPDATE", "CONTENT")
        data = []

        with sqlite3.connect(DB) as conn:
                data = read_entry(conn)
        table = self.query_one(DataTable)
        # Selection of data in row
        table.cursor_type = 'row'
        #table.zebra_stripes = True
        #table.loading = True
        table.tooltip = "Select a row to get more tips"
        #table.add_columns(*MY_DATA[0])
        #table.add_rows(MY_DATA[1:])
        table.add_columns(*title)
        table.add_rows(data)

    def select(self):
        cell = self.query_one(DataTable)
        row = cell.cursor_row

        data = cell.get_row_at(row)
        log.error(data)
        return data

    def sorts(self):
        pass
