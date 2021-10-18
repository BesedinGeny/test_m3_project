from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
import objectpack
from objectpack import tree_object_pack
from objectpack.actions import ObjectPack
from objectpack.ui import ModelEditWindow
from app import ui
from .controller import observer as obs
"""
class BaseObjectPack(ObjectPack):
    add_window = True
    can_delete = True
    add_window = edit_window = ModelEditWindow.fabricate(model)"""


class UserPack(ObjectPack):
    model = User
    add_to_desktop = True
    add_window = ui.UserAddWindow
    edit_window = ui.UserAddWindow
    #add_window = edit_window = ModelEditWindow.fabricate(model)
    can_delete = True


class ContentTypePack(ObjectPack):
    model = ContentType
    add_to_desktop = True
    can_delete = True
    add_window = edit_window = ModelEditWindow.fabricate(model)


class GroupPack(ObjectPack):
    model = Group
    add_to_desktop = True
    can_delete = True
    add_window = edit_window = ModelEditWindow.fabricate(model)


class PermissionPack(ObjectPack):
    model = Permission
    add_window = edit_window = ui.PermissionAddWindow #  Не нашел в доке чего-то типа Foriegn key  :((
    #add_window = edit_window = ModelEditWindow.fabricate(model) вызывает исключение, не разобрался как его исправить
    add_to_desktop = True
    can_delete = True



