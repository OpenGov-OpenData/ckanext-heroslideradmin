import pytest
import ckan.tests.factories as factories
import ckan.tests.helpers as helpers

from ckanext.heroslideradmin.db import init


@pytest.mark.ckan_config('ckan.plugins', 'heroslideradmin')
@pytest.mark.usefixtures('with_plugins')
class BaseTest(helpers.FunctionalTestBase):
    def setup(self):
        init()


class TestHeroSliderAdmin(BaseTest):
    def test_hero_slider_admin_form_exists(self, app):
        sysadmin = factories.Sysadmin()
        env = {"REMOTE_USER": sysadmin["name"]}
        response = app.get("/ckan-admin/hero_slider_admin", extra_environ=env)

        assert response.status_code == 200
        assert helpers.body_contains(response, "Manage Hero Slider")
        assert helpers.body_contains(response, "field-image-upload")
        assert helpers.body_contains(response, "image_upload_1")
        assert helpers.body_contains(response, "image_upload_2")
        assert helpers.body_contains(response, "image_upload_3")
        assert helpers.body_contains(response, "image_upload_4")
        assert helpers.body_contains(response, "image_upload_5")
