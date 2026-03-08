import { defineConfig } from 'vitepress'

// https://vitepress.dev/reference/site-config
export default defineConfig({
  title: "Pyside6 教程",
  description: "Pyside6",
  themeConfig: {
    // https://vitepress.dev/reference/default-theme-config
    nav: [
      { text: 'Home', link: '/' },
      { text: 'Examples', link: '/markdown-examples' }
    ],

    sidebar: [
      {
        text: '指南',
        items: [
          { text: '快速上手', link: '/guide/getting-started' },
          { text: '信号与插槽', link: '/guide/signals-and-slots' },
          { text: '布局', link: '/guide/layout' },
          { text: '样式', link: '/guide/styling' },
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
        ]
      }
    ],

    socialLinks: [
      { icon: 'github', link: 'https://github.com/xbzhang2020/python-gui-pyside6' }
    ]
  }
})
