class User:
    def __init__(self, id, username, email, password_hash, role, phone=None, address=None, shipping_company=None, industry_type=None, rating=0.0, profile_image=None):
        self.id = id
        self.username = username
        self.email = email
        self.password_hash = password_hash
        self.role = role
        self.phone = phone
        self.address = address
        self.shipping_company = shipping_company
        self.industry_type = industry_type
        self.rating = rating
        self.profile_image = profile_image

    def to_dict(self):
        return {
            "id": self.id,
            "username": self.username,
            "email": self.email,
            "role": self.role,
            "profile_image": self.profile_image
        }