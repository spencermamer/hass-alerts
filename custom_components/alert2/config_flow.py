import voluptuous as vol
from homeassistant import config_entries
from homeassistant.core import callback
from homeassistant.helpers import config_validation as cv

from . import DOMAIN

class Alert2ConfigFlow(config_entries.ConfigFlow, domain=DOMAIN):
    VERSION = 1

    @staticmethod
    @callback
    def async_get_options_flow(config_entry):
        return Alert2OptionsFlowHandler(config_entry)

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="Alert2", data=user_input)

        data_schema = vol.Schema({
            vol.Required("domain"): cv.string,
            vol.Required("name"): cv.string,
        })

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )

class Alert2OptionsFlowHandler(config_entries.OptionsFlow):
    def __init__(self, config_entry):
        self.config_entry = config_entry

    async def async_step_init(self, user_input=None):
        return await self.async_step_user()

    async def async_step_user(self, user_input=None):
        errors = {}
        if user_input is not None:
            return self.async_create_entry(title="", data=user_input)

        data_schema = vol.Schema({
            vol.Required("domain"): cv.string,
            vol.Required("name"): cv.string,
        })

        return self.async_show_form(
            step_id="user", data_schema=data_schema, errors=errors
        )
