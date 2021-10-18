from django.conf.urls import url
from objectpack import desktop
from .controller import controller
from . import  action

def register_urlpatterns():
    """
    Регистрация конфигурации урлов для приложения
    """
    return [url(*controller.urlpattern)]


def register_actions():
    """
    Регистрация экшен-паков
    """
    return controller.packs.extend([
        action.UserPack(),
        action.ContentTypePack(),
        action.GroupPack(),
        action.PermissionPack(),
    ])


def register_desktop_menu():
    """
    регистрация элементов рабочего стола
    """

    desktop.uificate_the_controller(
        controller,
        menu_root=desktop.MainMenu.SubMenu('Demo')
    )
