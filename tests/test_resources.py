"""
Tests for the resources sub-module.
"""
import securedrop_client.resources
from PyQt5.QtGui import QIcon, QPixmap
from PyQt5.QtSvg import QSvgWidget


def test_path(mocker):
    """
    Ensure the resource_filename function is called with the expected args and
    the path function under test returns its result.
    """
    r = mocker.patch('securedrop_client.resources.resource_filename',
                     return_value='bar')
    assert securedrop_client.resources.path('foo') == 'bar'
    r.assert_called_once_with(securedrop_client.resources.__name__,
                              'images/foo')


def test_load_icon():
    """
    Check the load_icon function returns the expected QIcon object.
    """
    result = securedrop_client.resources.load_icon('icon')
    assert isinstance(result, QIcon)


def test_load_svg():
    """
    Check the load_svg function returns the expected QSvgWidget object.
    """
    result = securedrop_client.resources.load_svg('paperclip.svg')
    assert isinstance(result, QSvgWidget)


def test_load_image():
    """
    Check the load_image function returns the expected QPixmap object.
    """
    result = securedrop_client.resources.load_image('icon')
    assert isinstance(result, QPixmap)


def test_load_css(mocker):
    """
    Ensure the resource_string function is called with the expected args and
    the load_css function returns its result.
    """
    rs = mocker.patch('securedrop_client.resources.resource_string',
                      return_value=b'foo')
    assert 'foo' == securedrop_client.resources.load_css('foo')
    rs.assert_called_once_with(securedrop_client.resources.__name__,
                               'css/foo')
