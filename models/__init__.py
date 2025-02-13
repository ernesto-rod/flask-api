from models.item import ItemModel as ItemModel
from models.item_tags import ItemTags as ItemTags
from models.store import StoreModel as StoreModel
from models.tag import TagModel as TagModel
from models.user import UserModel as UserModel


def main():
    _ = ItemModel()
    _ = StoreModel()
    _ = TagModel()
    _ = ItemTags()
    _ = UserModel()


if __name__ == "__main__":
    main()
