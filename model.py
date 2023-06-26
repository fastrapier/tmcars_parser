class Ad:
    def __init__(self):
        self._url = None
        self._title = None
        self._price = None
        self._descr = None
        self._city = None
        self._published = None

    @property
    def url(self):
        return self._url

    @url.setter
    def url(self, value):
        self._url = value

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, value):
        self._title = value

    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, value):
        self._price = value

    @property
    def descr(self):
        return self._descr

    @descr.setter
    def descr(self, value):
        self._descr = value

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        self._city = value

    @property
    def published(self):
        return self._published

    @published.setter
    def published(self, value):
        self._published = value

    def __iter__(self):
        return iter([self.published, self.title, self.price, self.city, self.descr, self.url])
