from core.db_singleton import DatabaseConnection
from models.user import User

class UserRepository:
    def __init__(self):
        self.connection = DatabaseConnection().get_connection()

    def add_user(self, username, email, password_hash, role, phone=None, address=None, shipping_company=None, industry_type=None):
        cursor = self.connection.cursor()
        query = """
            INSERT INTO users (username, email, password_hash, role, phone, address, shipping_company, industry_type) 
            VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """
        cursor.execute(query, (username, email, password_hash, role, phone, address, shipping_company, industry_type))
        self.connection.commit()
        cursor.close()

    def update_user(self, user_id, phone, address, shipping_company, industry_type, profile_image):
        cursor = self.connection.cursor()
        query = """
            UPDATE users 
            SET phone=%s, address=%s, shipping_company=%s, industry_type=%s, profile_image=%s
            WHERE id=%s
        """
        cursor.execute(query, (phone, address, shipping_company, industry_type, profile_image, user_id))
        self.connection.commit()
        cursor.close()

    def get_by_email(self, email):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE email = %s"
        cursor.execute(query, (email,))
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            return User(row['id'], row['username'], row['email'], row['password_hash'], row['role'], row['phone'], row['address'], row['shipping_company'], row['industry_type'], row['rating'], row['profile_image'])
        return None

    def get_by_id(self, user_id):
        cursor = self.connection.cursor(dictionary=True)
        query = "SELECT * FROM users WHERE id = %s"
        cursor.execute(query, (user_id,))
        row = cursor.fetchone()
        cursor.close()
        
        if row:
            return User(row['id'], row['username'], row['email'], row['password_hash'], row['role'], row['phone'], row['address'], row['shipping_company'], row['industry_type'], row['rating'], row['profile_image'])
        return None