from lib.post import Post

"""""
Test constructs Post class
"""

def test_post_constructs():
    post = Post(1,"Title","Contents")
    assert post.id == 1
    assert post.title == "Title"
    assert post.contents == "Contents"