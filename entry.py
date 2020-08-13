class Entry:

    def __init__(self, title, content, id):
        self.id = id
        self.title = title
        self.content = content

    def isValidEntry(self):
        self.title, self.content = self.title.strip(), self.content.strip()
        return len(self.title) > 0 and len(self.content) > 0

    def getContent(self):
        return self.content
    
    def getTitle(self):
        return self.title

    def setTitle(self, newTitle):
        self.title = newTitle

    def setContent(self, newContent):
        self.content = newContent
