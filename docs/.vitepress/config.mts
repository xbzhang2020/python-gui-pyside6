import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Pyside6 GUI 教程",
  description: "Pyside6",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: '指南', link: '/guide/getting-started' },
      // { text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: '指南',
        items: [
          { text: '快速上手', link: '/guide/getting-started' },
          { text: '信号与插槽', link: '/guide/signals-and-slots' },
          { text: '布局', link: '/guide/layout' },
          { text: '样式', link: '/guide/styling' },
          { text: '模型与视图', link: '/guide/model-and-view' },
        ]
      },
      {
        text: '常用组件',
        // collapsed: true,
        items: [
          { text: 'Label', link: '/widgets/label' },
          { text: 'Button', link: '/widgets/button' },
          { text: 'LineEdit', link: '/widgets/input' },
          { text: 'Slider', link: '/widgets/slider' },
          { text: 'List', link: '/widgets/list' },
          { text: 'Table', link: '/widgets/table' },
          { text: 'Tree', link: '/widgets/tree' },
          { text: 'MainWindow', link: '/widgets/main-window' },
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/xbzhang2020/python-gui-pyside6' }
    ]
  }
})
