/** @type {import('@docusaurus/plugin-content-docs').SidebarsConfig} */
const sidebars = {
  sdkSidebar: [
    {
      type: 'category',
      label: 'SDK',
      link: {type: 'doc', id: 'index'},
      items: ['api/mainboard', 'api/result', 'setup'],
    },
  ],
};

module.exports = sidebars;
