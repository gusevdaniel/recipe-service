from .base import metadata, engine
from .users import users
from .favourites import favorites
from .recipes import recipes
from .likes import likes
from .dishes import dishes
from .tags import tags
from .recipe_tags import recipe_tags

metadata.create_all(bind=engine)
