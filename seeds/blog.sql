-- As a blogger
-- So I can write interesting stuff
-- I want to write posts having a title.

-- As a blogger
-- So I can write interesting stuff
-- I want to write posts having a content.

-- As a blogger
-- So I can let people comment on interesting stuff
-- I want to allow comments on my posts.

-- As a blogger
-- So I can let people comment on interesting stuff
-- I want the comments to have a content.

-- As a blogger
-- So I can let people comment on interesting stuff
-- I want the author to include their name in comments.

-- Nouns
-- posts, title, post_content, comments, comment_content, commenter_name

-- posts:
-- id - SERIAL PRIMARY KEY
-- title - text
-- post_content - text

-- comments:
-- id - SERIAL
-- comment_content - text
-- commenter_name - text
-- post_id - SERIAL FOREIGN KEY

DROP TABLE IF EXISTS comments;
DROP SEQUENCE IF EXISTS comments_id_seq;
DROP TABLE IF EXISTS posts;
DROP SEQUENCE IF EXISTS posts_id_seq;


CREATE TABLE posts (
  id SERIAL PRIMARY KEY,
  title text,
  post_content text
);

CREATE TABLE comments (
  id SERIAL PRIMARY KEY,
  comment_content text,
  commenter_name text,
-- The foreign key name is always {other_table_singular}_id
  post_id int,
  constraint fk_post foreign key(post_id)
    references posts(id)
    on delete cascade
);

INSERT INTO posts (title, post_content) VALUES ('Python', 'Python is great!');
INSERT INTO posts (title, post_content) VALUES ('Javascript', 'Javascript is better.');

INSERT INTO comments (comment_content, commenter_name, post_id) VALUES ('No it is not', 'Oli', 1);
INSERT INTO comments (comment_content, commenter_name, post_id) VALUES ('I prefer Java', 'Usama', 1);
INSERT INTO comments (comment_content, commenter_name, post_id) VALUES ('I agree', 'Sam', 2);