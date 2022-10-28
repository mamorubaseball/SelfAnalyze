var path = require("path");
var webpack = require("webpack");
var BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  mode: "development",

  context: __dirname,

  entry: {
    main: "./src/main.js" // エントリ名とエントリポイント
  },

  output: {
    path: path.resolve("./assets/webpack_bundles/"), // 出力
    filename: "main.js"
  },

  plugins: [new BundleTracker({ filename: "./webpack-stats.json" })]
};
