import requests

class Post:
    def __init__(self, blog_id):
        self.blog_url = "https://api.npoint.io/4d1edc5c503fdb1b30a3"
        self.response = requests.get(url=self.blog_url)
        self.all_posts = self.response.json()
        self.blog_id = blog_id
        for post in self.all_posts:
            if post["id"] == self.blog_id:
                self.post = post
                break

