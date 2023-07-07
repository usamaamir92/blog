from lib.comment import Comment

"""""
Test constructs Comment class
"""

def test_comment_constructs():
    comment = Comment(1,"Comment whatever","Oli",1)

    assert comment.id == 1
    assert comment.comment_content == "Comment whatever"
    assert comment.commenter_name == "Oli"
    assert comment.post_id == 1