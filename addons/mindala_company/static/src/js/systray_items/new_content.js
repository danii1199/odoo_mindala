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
        moduleName: 'mindala_company',
        moduleXmlId: 'base.module_mindala_company',
        status: MODULE_STATUS.NOT_INSTALLED,
        icon: xml`<i class="fa fa-building-o"/>`,
        title: 'Empresas',
    },
    )
    const newBlogElement = this.state.newContentElements.find(
      (element) => element.moduleXmlId === 'base.module_mindala_company'
    );
    newBlogElement.createNewContent = () =>
      this.onAddContent('mindala_company.m4ocompany_action_add', true);
    newBlogElement.status = MODULE_STATUS.INSTALLED;
    newBlogElement.model = 'mindala.m4ocompany';
  },
});
