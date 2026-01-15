from core.db_singleton import DatabaseConnection
from models.listing import Listing

class ListingRepository:
    def __init__(self):
        self.connection = DatabaseConnection().get_connection()
    def add_listing(
        self,
        title,
        description,
        price,
        listing_type,
        image_url,
        producer_id,
        auction_end=None
    ):
        cursor = self.connection.cursor()
        query = """
            INSERT INTO listings
            (title, description, price, listing_type, image_url, producer_id, auction_end)
            VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(
            query,
            (
                title,
                description,
                price,
                listing_type,
                image_url,
                producer_id,
                auction_end
            )
        )
    
        self.connection.commit()
        cursor.close()


    def get_all_listings(self):
        cursor = self.connection.cursor(dictionary=True)
        query = """
            SELECT l.*, u.username as producer_name 
            FROM listings l
            JOIN users u ON l.producer_id = u.id
            ORDER BY l.created_at DESC
        """
        cursor.execute(query)
        rows = cursor.fetchall()
        cursor.close()
        
        listings = []
        for row in rows:
            listing = Listing(row['id'], row['title'], row['description'], row['price'], row['listing_type'], row['producer_id'], row['image_url'], row['created_at'], row['producer_name'])
            listings.append(listing)
        return listings

    def get_listing_by_id(self, listing_id):
        cursor = self.connection.cursor(dictionary=True)
        query = """
            SELECT l.*, u.username, u.phone, u.shipping_company, u.address, u.rating
            FROM listings l
            JOIN users u ON l.producer_id = u.id
            WHERE l.id = %s
        """
        cursor.execute(query, (listing_id,))
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            listing = Listing(row['id'], row['title'], row['description'], row['price'], row['listing_type'], row['producer_id'], row['image_url'], row['created_at'], row['username'])
            # Attach extra producer details dynamically
            listing.phone = row['phone']
            listing.shipping_company = row['shipping_company']
            listing.address = row['address']
            listing.producer_rating = row['rating']
            return listing
        return None