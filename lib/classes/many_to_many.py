class Article:
    all = []

    def __init__(self, author, magazine, title):
        if not isinstance(title, str) or len(title) < 5 or len(title) > 50:
            raise ValueError("Title must be a string between 5 and 50 characters inclusive")
        self._author = author
        self._magazine = magazine
        self.title = title
        Article.all.append(self)
        author._articles.append(self)
        magazine._articles.append(self)

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, value):
        if not isinstance(value, Author):
            raise ValueError("Author must be of type Author")
        self._author = value

    @property
    def magazine(self):
        return self._magazine

    @magazine.setter
    def magazine(self, value):
        if not isinstance(value, Magazine):
            raise ValueError("Magazine must be of type Magazine")
        self._magazine = value
class Author:
    def __init__(self, name):
        if not isinstance(name, str) or len(name) == 0:
            raise ValueError("Name must be a non-empty string")
        self._name = name
        self._articles = []

    @property
    def name(self):
        return self._name

    def articles(self):
        return self._articles

    def magazines(self):
        magazines = set()
        for article in self._articles:
            magazines.add(article.magazine)
        return list(magazines)

    def add_article(self, magazine, title):
       article = Article(self, magazine, title)
       if article not in self._articles:
        self._articles.append(article)
        magazine._articles.append(article)
       return article

    def topic_areas(self):
     categories = set()
     for article in self._articles:
        categories.add(article.magazine.category)
     return list(categories) if categories else []

class Magazine:
    def __init__(self, name, category):
        if not isinstance(name, str) or not 2 <= len(name) <= 16:
            raise ValueError("Name must be a string between 2 and 16 characters inclusive")
        if not isinstance(category, str) or len(category) == 0:
            raise ValueError("Category must be a non-empty string")
        self._name = name
        self._category = category
        self._articles = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if not isinstance(value, str) or not 2 <= len(value) <= 16:
            raise ValueError("Name must be a string between 2 and 16 characters inclusive")
        self._name = value

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, value):
        if not isinstance(value, str) or len(value) == 0:
            raise ValueError("Category must be a non-empty string")
        self._category = value

    def articles(self):
        return self._articles

    def contributors(self):
        authors = set()
        for article in self._articles:
            authors.add(article.author)
        return list(authors)

    def article_titles(self):
        return [article.title for article in self._articles] if self._articles else None

    def contributing_authors(self):
        authors = set()
        for article in self._articles:
            authors.add(article.author)
        contributing_authors = [author for author in authors if len([article for article in self._articles if article.author == author]) > 2]
        return list(contributing_authors) if contributing_authors else None