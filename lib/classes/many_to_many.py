class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str):
            raise ValueError("Title must be a string")
        self._title = title
        self.author = author
        self.magazine = magazine
        Article.all.append(self)

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        raise AttributeError("Cannot set attribute 'title'")


class Author:
    def __init__(self, name):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if len(name) == 0:
            raise ValueError("Name must have more than 0 characters")
        self._name = name
        self._articles = []
        self._magazines = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        raise ValueError("Cannot change author's name")

    def articles(self):
        return [article for article in Article.all if article.author == self]

    def magazines(self):
        return list(set(article.magazine for article in Article.all if article.author == self))

    def add_article(self, magazine, title):
        return Article(self, magazine, title)

    def topic_areas(self):
        categories = {article.magazine.category for article in Article.all if article.author == self}
        return list(categories) if categories else None


class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str):
            raise ValueError("Name must be a string")
        if not isinstance(category, str):
            raise ValueError("Category must be a string")
        if not 2 <= len(name) <= 16:
            raise ValueError("Name must be between 2 and 16 characters long")
        if not category:
            raise ValueError("Category cannot be empty")
        self._name = name
        self._category = category

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str):
            raise ValueError("Name must be a string")
        if not 2 <= len(value) <= 16:
            raise ValueError("Name must be between 2 and 16 characters long")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str):
            raise ValueError("Category must be a string")
        if not value:
            raise ValueError("Category cannot be empty")
        self._category = value

    def articles(self):
        return [article for article in Article.all if article.magazine == self]

    def contributors(self):
        return list(set(article.author for article in Article.all if article.magazine == self))

    def article_titles(self):
        titles = [article.title for article in Article.all if article.magazine == self]
        return titles or None

    def contributing_authors(self):
        author_article_count = {}
        for article in self.articles():
            author_name = article.author.name
            author_article_count[author_name] = author_article_count.get(author_name, 0) + 1
        return [author for author in set(article.author for article in self.articles()) 
                if author_article_count.get(author.name, 0) > 2] or None