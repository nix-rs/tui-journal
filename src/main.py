from journal import Journal
from database import db

# FIX: Change date formatting
# FIX: hide ID on read
# FIX: Make colorful the app
# FIX: Encrypt the database
# FIX: update the read on realtime **
# FIX: Move scroll bar with cursor when moving in read **
# FIX: make package installation on all distro via pip
# FIX: setup config for linux
# FIX: Implement sorting on read **
# FIX: Search based on Tags and date **
# FIX: Markdown View
# textual run --dev myapp.py


if __name__ == "__main__":
    db()
    app = Journal()
    app.run()

