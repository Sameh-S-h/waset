class Listing:
    def __init__(self, id, title, description, price, listing_type, producer_id, image_url=None, created_at=None, producer_name=None):
        self.id = id
        self.title = title
        self.description = description
        self.price = price
        self.listing_type = listing_type
        self.producer_id = producer_id
        self.image_url = image_url
        self.created_at = created_at
        self.producer_name = producer_name