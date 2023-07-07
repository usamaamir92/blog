class Post():
    def __init__(self,id,title,contents,comments=None):
        self.id = id
        self.title = title
        self.contents = contents
        self.comments = comments or []

    def __eq__(self,other):
        return self.__dict__ == other.__dict__