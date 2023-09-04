odoo.define("mindala_news.tour", function (require) {
    "use strict";

    const {_t} = require("web.core");
    const {Markup} = require('web.utils');
    const wTourUtils = require('website.tour_utils');

    wTourUtils.registerWebsitePreviewTour("m4pnews", {
        url: "/",
    }, [{
        trigger: "body:not(:has(#o_new_content_menu_choices)) .o_new_content_container > a",
        content: _t("Click here to add new content to your website."),
        consumeVisibleOnly: true,
        position: 'bottom',
    }, {
        trigger: 'a[data-module-xml-id="base.module_mindala_news"]',
        content: _t("Select this menu item to create a new blog post."),
        position: "bottom",
    }, {
        trigger: 'div[name="name"] input',
        content: _t("Enter your post's title"),
        position: "bottom",
    },
]);
});
