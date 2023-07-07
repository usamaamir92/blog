from lib.post_repository import PostRepository
from lib.comment import Comment
from lib.post import Post

def test_get_all_comments_for_post(db_connection):
    db_connection.seed("seeds/blog.sql")

    repository = PostRepository(db_connection)
    comments = repository.comments_by_post(1)

    assert comments == Post(1,'Python', 'Python is great!',[Comment(1,'No it is not', "Oli", 1),
                        Comment(2,'I prefer Java', "Usama", 1)])
    