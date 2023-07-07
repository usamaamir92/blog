from lib.comment import Comment
from lib.post import Post

class PostRepository():
    def __init__(self,connection):
        self.connection = connection


    def comments_by_post(self,post):
        rows = self.connection.execute("""SELECT *
                                       FROM posts
                                       JOIN comments ON comments.post_id = posts.id
                                       WHERE posts.id = %s""",[post])
        print(rows)

        comments = []
        for row in rows:
            comment = Comment(row["id"],row["comment_content"],row["commenter_name"],row["post_id"])
            comments.append(comment)
        post = Post(rows[0]["id"],rows[0]["title"],rows[0]["post_content"],comments)

        return post