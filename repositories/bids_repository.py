# from core.db_singleton import get_db_connection
from core.db_singleton import DatabaseConnection

class BidRepository:
    def place_bid(self, listing_id, bidder_id, amount):
        conn = DatabaseConnection().get_connection()

        cursor = conn.cursor()

        query = """
        INSERT INTO bids (listing_id, bidder_id, bid_amount)
        VALUES (%s, %s, %s)
        """
        cursor.execute(query, (listing_id, bidder_id, amount))
        conn.commit()

    def get_highest_bid(self, listing_id):
        conn = DatabaseConnection().get_connection()
        cursor = conn.cursor(dictionary=True)

        query = """
        SELECT MAX(bid_amount) AS highest_bid
        FROM bids
        WHERE listing_id = %s
        """
        cursor.execute(query, (listing_id,))
        return cursor.fetchone()["highest_bid"]
