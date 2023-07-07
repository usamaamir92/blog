class Comment():
    def __init__(self,id,comment_content,commenter_name,post_id):
        self.id = id
        self.comment_content = comment_content
        self.commenter_name = commenter_name
        self.post_id = post_id

    def __eq__(self,other):
        return self.__dict__ == other.__dict__