class Band:
    def __init__(self, name, hometown):
        self.name = name
        self.hometown = hometown
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def hometown(self):
        return self._hometown

    @hometown.setter
    def hometown(self, value):
        if not hasattr(self, '_hometown'):
            if isinstance(value, str) and len(value) > 0:
                self._hometown = value
            else:
                raise ValueError("Hometown must be a non-empty string")
        else:
            raise AttributeError("Hometown cannot be changed after it's set")

    def add_concert(self, concert):
        if isinstance(concert, Concert):
            self._concerts.append(concert)
        else:
            raise ValueError("Concert must be an instance of the Concert class")

    @property
    def concerts(self):
        return self._concerts if self._concerts else None

    @property
    def venues(self):
        if not self._concerts:
            return None
        return list(set(concert.venue for concert in self._concerts))

    def play_in_venue(self, venue, date):
        return Concert(date, self, venue)

    def all_introductions(self):
        if not self._concerts:
            return None
        return [concert.introduction() for concert in self._concerts]


class Venue:
    def __init__(self, name, city):
        self.name = name
        self.city = city
        self._concerts = []

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._name = value
        else:
            raise ValueError("Name must be a non-empty string")

    @property
    def city(self):
        return self._city

    @city.setter
    def city(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._city = value
        else:
            raise ValueError("City must be a non-empty string")

    def add_concert(self, concert):
        if isinstance(concert, Concert):
            self._concerts.append(concert)
        else:
            raise ValueError("Concert must be an instance of the Concert class")

    def concerts(self):
        return self._concerts if self._concerts else None

    def bands(self):
        if not self._concerts:
            return None
        return list(set(concert.band for concert in self._concerts))


class Concert:
    def __init__(self, date, band, venue):
        self.date = date
        self.band = band
        self.venue = venue
        band.add_concert(self)
        venue.add_concert(self)

    @property
    def date(self):
        return self._date

    @date.setter
    def date(self, value):
        if isinstance(value, str) and len(value) > 0:
            self._date = value
        else:
            raise ValueError("Date must be a non-empty string")

    @property
    def band(self):
        return self._band

    @band.setter
    def band(self, value):
        if isinstance(value, Band):
            self._band = value
        else:
            raise ValueError("Band must be an instance of the Band class")

    @property
    def venue(self):
        return self._venue

    @venue.setter
    def venue(self, value):
        if isinstance(value, Venue):
            self._venue = value
        else:
            raise ValueError("Venue must be an instance of the Venue class")

    def hometown_show(self):
        return self.venue.city == self.band.hometown

    def introduction(self):
        return f"Hello {self.venue.city}!!!!! We are {self.band.name} and we're from {self.band.hometown}"
