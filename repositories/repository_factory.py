from repositories.user_repository import UserRepository
from repositories.listing_repository import ListingRepository
from repositories.bids_repository import BidRepository


class RepositoryFactory:

    @staticmethod
    def get_repository(repo_type):
        if repo_type == "user":
            return UserRepository()
        if repo_type == "listing":
            return ListingRepository()
        raise ValueError("Unknown repository type")

    @staticmethod
    def get_bid_repository():
        return BidRepository()
