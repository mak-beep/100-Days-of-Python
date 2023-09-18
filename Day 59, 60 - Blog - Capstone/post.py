class Post:
    def __init__(self, new_post):
        self.title = new_post['title']
        self.body = new_post['body']
        self.id = new_post['id']
        self.subtitle = new_post['subtitle']
