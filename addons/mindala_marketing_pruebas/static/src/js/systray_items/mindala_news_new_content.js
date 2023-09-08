/** @odoo-module **/
import {
  NewContentModal,
  MODULE_STATUS,
} from '@website/systray_items/new_content';
import { patch } from 'web.utils';

const { Component, xml, useState, onWillStart } = owl;

patch(NewContentModal.prototype, 'mindala_marketing_new_content', {
  setup() {
    this._super();
    this.state.newContentElements.push(
    {
        moduleName: 'mindala_marketing',
        moduleXmlId: 'base.module_mindala_marketing',
        status: MODULE_STATUS.NOT_INSTALLED,
        icon: xml`<i class="fa fa-newspaper-o"/>`,
        title: 'News',
    },
    )
    const newBlogElement = this.state.newContentElements.find(
      (element) => element.moduleXmlId === 'base.module_mindala_marketing'
    );
    newBlogElement.createNewContent = () =>
      this.onAddContent('mindala_marketing.mindala_news_action_add', true);
    newBlogElement.status = MODULE_STATUS.INSTALLED;
    newBlogElement.model = 'mindala.news';
  },
});
