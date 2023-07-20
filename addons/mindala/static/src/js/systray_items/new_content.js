/** @odoo-module **/

import {
  NewContentModal,
  MODULE_STATUS,
} from '@website/systray_items/new_content';
import { patch } from 'web.utils';

patch(NewContentModal.prototype, 'mindala_m4pnews_new_content', {
  setup() {
    this._super();

    const newBlogElement = this.state.newContentElements.find(
      (element) => element.moduleXmlId === 'base.module_website_blog_news'
    );
    newBlogElement.createNewContent = () =>
      this.onAddContent('mindala.blog_m4pnews_action_add', true);
    newBlogElement.status = MODULE_STATUS.INSTALLED;
    newBlogElement.model = 'blog.m4pnews';
  },
});
