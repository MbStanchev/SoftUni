class Comment():
    def __init__(self, username, content, likes =0):
        self.name = username
        self.content = content
        self.likes = likes

comment = Comment("user1", "I like this book")
print(comment.name)
print(comment.content)
print(comment.likes)
