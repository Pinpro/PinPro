module.exports = {
  root: true,
  env: {
    node: true,
  },
  extends: [
    'plugin:vue/essential',
    '@vue/airbnb',
  ],
  rules: {
    // 'no-console': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'no-debugger': process.env.NODE_ENV === 'production' ? 'error' : 'off',
    'max-len': 'off',
    'no-console': 'off',
    'global-require': 0,//Unexpected require() (global-require)解决vue项目使用require() 编译报错 
  },
  parserOptions: {
    parser: 'babel-eslint',
  },
};
