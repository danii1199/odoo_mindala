/** @odoo-module **/

import {
  NewContentModal,
  MODULE_STATUS,
} from '@website/systray_items/new_content';
import { patch } from 'web.utils';

const { Component, xml, useState, onWillStart } = owl;

patch(NewContentModal.prototype, 'mindala_m4pnews_new_content', {
  setup() {
    this._super();
    console.log(this.state);
    console.log(this.state.newContentElements);
    this.state.newContentElements.push(
    {
        moduleName: 'website_m4pnews',
        moduleXmlId: 'base.module_website_m4pnews',
        status: MODULE_STATUS.NOT_INSTALLED,
        icon: xml`<i class="fa fa-newspaper-o"/>`,
        title: 'Noticias',
    },
    )
    const newBlogElement = this.state.newContentElements.find(
      (element) => element.moduleXmlId === 'base.module_website_m4pnews'
    );
    newBlogElement.createNewContent = () =>
      this.onAddContent('mindala.blog_m4pnews_action_add', true);
    newBlogElement.status = MODULE_STATUS.INSTALLED;
    newBlogElement.model = 'blog.m4pnews';
  },
});
